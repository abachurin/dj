from django.db import models
from sorl.thumbnail import ImageField


class C1(models.Model):
    text = models.CharField(max_length=20, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.text

