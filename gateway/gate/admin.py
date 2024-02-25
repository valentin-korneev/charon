from django.contrib import admin
from custom.link_to_obj import link_to_obj
from gateway.gate.model import Gate


@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_group', 'get_chat']
    list_filter = ['group', 'chat']

    @admin.display(description='Group')
    def get_group(self, obj):
        return link_to_obj('receiver', 'group', obj.group_id, obj.group)

    @admin.display(description='Chat')
    def get_chat(self, obj):
        return link_to_obj('telegram', 'chat', obj.chat_id, obj.chat)
