from django.db import models
from gateway.gate.model import Gate


class Rule(models.Model):

    class Type(models.TextChoices):
        CONTAIN = 'contain', 'Contain'
        REGEX = 'regex', 'Regex'
        MASK = 'mask', 'Mask'

    type = models.CharField(choices=Type.choices, max_length=10)
    name = models.CharField(max_length=256)
    pattern = models.TextField()
    is_active = models.BooleanField(default=True)
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        name = self.name

        if self.gate:
            name += ' ({})'.format(self.gate)

        return name

