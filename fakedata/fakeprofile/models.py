from django.db import models

# Create your models here.
class Profile(models.Model):
    """Model definition for profile."""

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)

    class Meta:
        """Meta definition for profile."""

        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        """Unicode representation of profile."""
        pass
