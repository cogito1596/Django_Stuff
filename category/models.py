from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

# Create your models here.


class category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to="photos/categories", blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)
