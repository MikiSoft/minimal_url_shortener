from django.db import models
from django.utils.crypto import get_random_string


def generate_slug():
    return get_random_string(8)

class URL(models.Model):
    slug = models.CharField(unique=True, default=generate_slug, max_length=8)
    original_link = models.CharField(max_length=1024)

    def __str__(self):
        return self.slug+': '+self.original_link