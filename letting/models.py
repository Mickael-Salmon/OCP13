from django.db import models
from oc_letting_site.models import Address


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Meta:
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"