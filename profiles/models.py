from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    A model representing a user profile.

    Attributes:
        user (User): The user associated with this profile.
        favorite_city (str): The user's favorite city.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
