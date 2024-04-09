from django.db import models
from gateway.gate.model import Gate
from receiver.message.model import Message as MainMessage


class Message(models.Model):
    message = models.ForeignKey(MainMessage, on_delete=models.CASCADE)
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE)
    content = models.TextField()
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({})'.format(self.message, self.id)

    class Meta:
        default_permissions = ['view']
