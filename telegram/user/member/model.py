from django.db import models
from telegram.user.model import User


class Member(User):
    @classmethod
    def parse_and_save(cls, obj):
        member, created = Member.objects.update_or_create(
            id=obj.get('id'),
            defaults={
                'first_name': obj.get('first_name'),
                'last_name': obj.get('last_name'),
                'username': obj.get('username'),
            }
        )
        return member

    class Meta:
        default_permissions = ['view']
