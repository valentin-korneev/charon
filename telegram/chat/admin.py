from django.contrib import admin

from custom.link_to_obj import link_to_obj
from telegram.chat.model import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'title', 'member_count', 'get_bot']
    list_filter = ['type', 'bot']

    def has_delete_permission(self, request, obj=None):
        return False

    @staticmethod
    def member_count(obj):
        return obj.members.count()

    @admin.display(description='Bot')
    def get_bot(self, obj):
        return link_to_obj('telegram', 'bot', obj.bot_id, obj.bot)
