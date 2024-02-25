from django.contrib import admin

from custom.link_to_obj import link_to_obj
from gateway.rule.model import Rule


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'is_active', 'pattern', 'get_gate']
    list_filter = ['gate__group', 'gate__chat', 'is_active']

    @admin.display(description='Gate')
    def get_gate(self, obj):
        return link_to_obj('gateway', 'gate', obj.gate_id, obj.gate) if obj.gate_id else None
