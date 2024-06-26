from django.db import models
from receiver.group.model import Group
from telegram.chat.model import Chat


class Gate(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['group', 'chat']

    def __str__(self):
        return '{} => {}'.format(self.group, self.chat)

