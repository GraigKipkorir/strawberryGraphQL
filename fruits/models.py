from django.db import models
from django_choices_field import TextChoicesField

class FruitCategory(models.TextChoices):
    CITRUS = "citrus","Citrus"
    