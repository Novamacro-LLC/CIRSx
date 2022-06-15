from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=150, null=False)
    event_start_dt = models.DateField(null=False)
    event_end_dt = models.DateField(null=False)
    event_location = models.CharField(max_length=150, null=False)


class Audience(models.Model):
    aud_name = models.CharField(max_length=50, unique=True, null=False)
    aud_desc = models.CharField(max_length=150, null=False)


class DocumentType(models.Model):
    doctyp_name = models.CharField(max_length=50, unique=True, null=False)
    doctyp_desc = models.CharField(max_length=150, null=False)


class Documents(models.Model):
    title = models.CharField(max_length=200, null=False)



