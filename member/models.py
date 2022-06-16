from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=150, null=False)
    event_start_dt = models.DateField(null=False)
    event_end_dt = models.DateField(null=False)
    event_location = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.event_name


class Audience(models.Model):
    aud_name = models.CharField(max_length=50, unique=True, null=False)
    aud_desc = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.aud_name


class DocumentType(models.Model):
    doctyp_name = models.CharField(max_length=50, unique=True, null=False)
    doctyp_desc = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.doctyp_name


class Document(models.Model):
    doctyp_num = models.ForeignKey(DocumentType, null=True, on_delete=models.SET_NULL)
    aud_num = models.ForeignKey(Audience, null=True, on_delete=models.SET_NULL)
    doc_path = models.CharField(max_length=250)
    title = models.CharField(max_length=500, null=False)
    author = models.CharField(max_length=150, null=True)
    keywords = models.CharField(max_length=250, null=True)
    pub_dt = models.DateField(null=True)
    doc_abs = models.TextField(null=True)
    doc_txt = models.TextField(null=True)

    def __str__(self):
        return self.title
