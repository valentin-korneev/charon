from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
