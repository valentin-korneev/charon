from django.contrib import admin
from telegram.user.bot.model import Bot


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    exclude = ['first_name', 'last_name', 'username', 'last_update_id']
    list_display = ['id', 'first_name', 'last_name', 'username']
