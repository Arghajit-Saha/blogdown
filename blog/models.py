from django.db import models
from django.utils.text import slugify
import datetime

class Create(models.Model):
    title = models.CharField()
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    message = models.TextField()
