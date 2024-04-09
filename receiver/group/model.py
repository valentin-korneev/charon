from django.db import models
from receiver.application.model import Application


PERM_GENERATE_TOKEN = 'generate_token'


class Group(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [(PERM_GENERATE_TOKEN, 'Can generate token')]
