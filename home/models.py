from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField


class News(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Communication(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=250, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.subject



