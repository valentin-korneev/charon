import uuid
from django.db import models
from receiver.group.model import Group


class Token(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, unique=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)

    @property
    def masked_token(self):
        parts = [part for part in self.token.split('-')]
        return '-'.join(
            [str(part if i in [0, len(parts) - 1] else ('*' * len(part))) for i, part in enumerate(parts)]
        )

    def __str__(self):
        return self.masked_token

    class Meta:
        default_permissions = ['view', 'delete']


