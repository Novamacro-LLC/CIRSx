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


class Expertise(models.Model):
    expertise_code = models.CharField(max_length=20, unique=True)
    expertise_desc = models.CharField(max_length=150)

    def __str__(self):
        return self.expertise_code


class Speakers(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=75, null=False)
    state = models.CharField(max_length=2, null=False)
    zip = models.CharField(max_length=10, null=False)
    country = models.CharField(max_length=3, null=False)
    expertise = models.ForeignKey(Expertise)
    credentials = models.TextField(null=False)
    bio = models.TextField(null=False)
    image = models.ImageField(upload_to=None, width_field=None, height_field=None, max_length=100)

    def __str__(self):
        return self.last_name + "," + self.first_name
