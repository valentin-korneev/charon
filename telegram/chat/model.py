from django.db import models
from telegram.user.bot.model import Bot
from telegram.user.member.model import Member


class Chat(models.Model):

    class Type(models.TextChoices):
        PRIVATE = 'private', 'Private'
        GROUP = 'group', 'Group'
        SUPERGROUP = 'supergroup', 'Super Group'
        CHANNEL = 'channel', 'Channel'

    type = models.CharField(max_length=10, choices=Type.choices)
    title = models.CharField(null=True, blank=True, max_length=256)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, related_name='chats', blank=True)

    @classmethod
    def parse_and_save(cls, obj, bot):
        chat, created = Chat.objects.update_or_create(
            id=obj.get('id'),
            defaults={
                'type': obj.get('type'),
                'bot': bot,
                'title': Chat.get_full_name(
                    obj.get('title'),
                    obj.get('first_name'),
                    obj.get('last_name'),
                    obj.get('username'),
                ),
            }
        )
        return chat

    @staticmethod
    def get_full_name(title=None, first_name=None, last_name=None, username=None):
        full_name = ''

        if title is not None:
            full_name = title
        elif first_name is not None:
            full_name = 'Chat with {}'.format(first_name)
            if last_name is not None:
                full_name += ' ' + last_name
            if username is not None:
                full_name += ' ({})'.format(username)

        return full_name

    def __str__(self):
        return self.title

    def send_message(self, message):
        self.bot.request('sendMessage', params={
            'chat_id': self.id,
            'text': message
        })

    class Meta:
        default_permissions = ['add', 'change', 'view']

