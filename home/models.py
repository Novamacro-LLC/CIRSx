from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

class news(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.CharField(max_length=175, default="Transparent-gold.jpg")
    date_added = models.DateTimeField(default=timezone.now)
    user = CurrentUserField()