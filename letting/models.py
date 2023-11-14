from django.db import models
from oc_letting_site.models import Address
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User

class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
