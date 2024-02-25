from django.contrib import admin
from custom.link_to_obj import link_to_obj
from receiver.message.model import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_application', 'get_group', 'get_content', 'created']
    list_filter = ['group__application', 'group']
    search_fields = ['content']

    def get_actions(self, request):
        return {}

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    @admin.display(description='Application')
    def get_application(self, obj):
        return link_to_obj('receiver', 'application', obj.group.application_id, obj.group.application)

    @admin.display(description='Group')
    def get_group(self, obj):
        return link_to_obj('receiver','group', obj.group_id, obj.group)

    @staticmethod
    @admin.display(description='Content')
    def get_content(obj):
        return f'{obj.content[:50]}...' if len(obj.content) > 53 else obj.content
