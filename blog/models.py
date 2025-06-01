from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Create(models.Model):
    title = models.CharField()
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
