from django.contrib import admin
from telegram.user.member.model import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'chat_count')
    list_filter = ['chats']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    @staticmethod
    def chat_count(obj):
        return obj.chats.count()
