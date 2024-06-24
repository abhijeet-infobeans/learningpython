from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    """Model definition for Country."""

    name = models.CharField(max_length=80)
    code = models.CharField(max_length=5)

    class Meta:
        """Meta definition for Country."""

        verbose_name = 'Country'
        verbose_name_plural = 'Countrys'

    def __str__(self):
        """Unicode representation of Country."""
        return f'{self.name}'


class Address(models.Model):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)

    def full_address(self):
        return f'{self.address_line1} {self.address_line2}'

    def __str__(self) -> str:
        return self.full_address()
    
    class Meta:
        verbose_name_plural = 'Address Entries'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        null=True
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True, blank=True)
    published_countries = models.ManyToManyField("Country")

    def __str__(self) -> str:
        return f'{self.title} ({self.rating}) ({self.author}) ({self.is_bestselling})'
