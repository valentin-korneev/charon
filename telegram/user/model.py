from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(null=True, blank=True, max_length=256)
    username = models.CharField(null=True, blank=True, max_length=256)

    class Meta:
        abstract = True

    def __str__(self):
        full_name = self.first_name

        if self.last_name:
            full_name += f' {self.last_name}'

        return full_name
