from django.contrib import admin

from custom.link_to_obj import link_to_obj
from gateway.message.model import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_message', 'get_gate', 'content', 'is_blocked']
    list_filter = ['gate__group', 'gate__chat', 'is_blocked']
    search_fields = ['content', 'message__content']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    @admin.display(description='Gate')
    def get_gate(self, obj):
        return link_to_obj('gateway', 'gate', obj.gate_id, obj.gate)

    @admin.display(description='Message')
    def get_message(self, obj):
        return link_to_obj('receiver', 'message', obj.message_id, obj.message)
