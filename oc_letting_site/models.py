from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A model representing a physical address.

    Attributes:
        number (PositiveIntegerField): The street number of the address.
        street (CharField): The name of the street.
        city (CharField): The name of the city.
        state (CharField): The two-letter abbreviation for the state.
        zip_code (PositiveIntegerField): The ZIP code of the address.
        country_iso_code (CharField): The three-letter ISO code for the country.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
