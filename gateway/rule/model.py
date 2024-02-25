from django.db import models
from gateway.gate.model import Gate


class Rule(models.Model):
    RULE_TYPE_CONTAIN = 'contain'
    RULE_TYPE_REGEX = 'regex'
    RULE_TYPE_MASK = 'mask'

    RULE_TYPES = (
        (RULE_TYPE_CONTAIN, 'Contain'),
        (RULE_TYPE_REGEX, 'Regex'),
        (RULE_TYPE_MASK, 'Mask'),
    )

    id = models.BigAutoField(primary_key=True, editable=False)
    type = models.CharField(choices=RULE_TYPES, max_length=10)
    name = models.CharField(max_length=256)
    pattern = models.TextField()
    is_active = models.BooleanField(default=True)
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        name = self.name

        if self.gate:
            name += f' ({self.gate})'

        return name

