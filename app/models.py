from django.db import models

from django.utils import timezone

# Create your models here.


class Counter(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateTimeField(
        default=timezone.now, blank=False, null=False)

    def __str__(self):
        return self.name
