from django.contrib import admin
from custom.link_to_obj import link_to_obj
from receiver.group.model import Group, PERM_GENERATE_TOKEN


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_application', 'name', 'description']
    actions = ['generate_token']
    list_filter = ['application']
    ordering = ['name']

    @admin.action(description='Generate token', permissions=[PERM_GENERATE_TOKEN])
    def generate_token(self, request, queryset):
        from receiver.token.model import Token

        for group in queryset:
            token = Token.objects.create(group=group)
            self.message_user(request, f'Token for {group}: {token.token}')

    @admin.display(description='Application')
    def get_application(self, obj):
        return link_to_obj('receiver', 'application', obj.application_id, obj.application)

    @staticmethod
    def has_generate_token_permission(request):
        return request.user.has_perm('receiver' + PERM_GENERATE_TOKEN)
