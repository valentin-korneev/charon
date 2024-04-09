from django.db import models
from receiver.group.model import Group


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        default_permissions = ['view']

