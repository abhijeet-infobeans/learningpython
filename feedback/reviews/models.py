from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    """Model definition for Review."""

    user_name = models.CharField(max_length=10)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of Review."""
        return f'{self.name} ({self.rating})'
