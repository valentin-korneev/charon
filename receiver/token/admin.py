from django.contrib import admin
from custom.link_to_obj import link_to_obj
from receiver.token.model import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_application', 'get_group', 'masked_token', 'is_active']
    fields = ['id', 'group', 'masked_token', 'is_active']
    actions = ['redeem']
    list_filter = ['group__application', 'group', 'is_active']
    ordering = ['-is_active', 'id']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    @admin.action(description='Redeem', permissions=['delete'])
    def redeem(self, request, queryset):
        for token in queryset:
            token.is_active = False
            token.save()

    @admin.display(description='Application')
    def get_application(self, obj):
        return link_to_obj('receiver', 'application', obj.group.application_id, obj.group.application)

    @admin.display(description='Group')
    def get_group(self, obj):
        return link_to_obj('receiver', 'group', obj.group_id, obj.group)

