from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField


class News(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.CharField(max_length=175, default="Transparent-gold.jpg")
    date_added = models.DateTimeField(default=timezone.now)
    user = CurrentUserField()


class Communication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
