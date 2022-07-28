from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField


class News(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
 #   image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
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


class Team(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    credentials = models.CharField(max_length=10, null=True)
    founder = models.BooleanField()
    title = models.CharField(max_length=50, null=False)
    active = models.BooleanField()

    def __str__(self):
        return self.last_name + "," + self.first_name


class StrategicPartner(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    credentials = models.CharField(max_length=10, null=True)
    active = models.BooleanField()

    def __str__(self):
        return self.last_name + "," + self.first_name


class SupportPartners(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    url = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.company_name
