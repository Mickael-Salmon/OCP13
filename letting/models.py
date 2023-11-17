from django.db import models
from oc_letting_site.models import Address


class Letting(models.Model):
    """
    A class representing a letting.

    Attributes:
    -----------
    title : str
        The title of the letting.
    address : Address
        The address of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Meta:
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"