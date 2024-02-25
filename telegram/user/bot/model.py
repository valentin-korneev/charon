import json
from django.core.exceptions import ValidationError
from django.db import models
from requests import get
from telegram.user.member.model import Member
from telegram.user.model import User


class Bot(User):
    UPDATE_CHAT_MEMBER = 'chat_member'
    UPDATE_MESSAGE = 'message'
    UPDATE_CHANNEL_POST = 'channel_post'

    token = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    last_update_id = models.BigIntegerField(default=0)

    def request(self, method, params=None):
        response = get(
            f'https://api.telegram.org/bot{self.token}/{method}',
            params=params
        )
        response_json = response.json()

        if response_json.get('ok', False):
            return response_json.get('result')
        else:
            raise Exception(f'Telegram: {response_json.get("error_code")} - {response_json.get("description")}')

    def get_me_by_token(self):
        user = self.request('getMe')

        if not user.get('is_bot'):
            raise Exception(f'Telegram: User {user.get("first_name")} is not Bot')

        self.id = user.get('id')
        self.first_name = user.get('first_name')
        self.last_name = user.get('last_name')
        self.username = user.get('username')

    def get_updates(self):
        last_update_id = self.last_update_id
        updates = self.request('getUpdates', params={
            'offset': last_update_id + 1,
            'limit': 100,
            'allowed_updates': json.dumps([
                Bot.UPDATE_CHAT_MEMBER,
                Bot.UPDATE_MESSAGE,
                Bot.UPDATE_CHANNEL_POST,
            ])
        })

        for update in updates:
            last_update_id = max(last_update_id, update.get('update_id'))

            if Bot.UPDATE_CHAT_MEMBER in update:
                self._chat_member(update.get(Bot.UPDATE_CHAT_MEMBER))
            if Bot.UPDATE_MESSAGE in update:
                self._message(update.get(Bot.UPDATE_MESSAGE))
            if Bot.UPDATE_CHANNEL_POST in update:
                self._channel_post(update.get(Bot.UPDATE_CHANNEL_POST))

        return last_update_id

    def clean(self):
        try:
            self.get_me_by_token()
        except Exception as e:
            raise ValidationError(e)

    def _chat_member(self, obj):
        from telegram.chat.model import Chat

        chat = Chat.parse_and_save(obj.get('chat'), self)

        obj = obj.get('new_chat_member')
        member = Member.parse_and_save(obj.get('user'))
        is_active = obj.get('status') == 'member'

        if (member in chat.members.all()) != is_active:
            if is_active:
                chat.members.add(member)
            else:
                chat.members.remove(member)

    def _message(self, obj):
        from telegram.chat.model import Chat

        chat = Chat.parse_and_save(obj.get('chat'), self)
        member = Member.parse_and_save(obj.get('from'))

        if member not in chat.members.all():
            chat.members.add(member)

    def _channel_post(self, obj):
        from telegram.chat.model import Chat

        Chat.parse_and_save(obj.get('chat'), self)
