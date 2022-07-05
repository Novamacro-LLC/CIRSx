from django.db import models
from account.models import Account


class Country(models.Model):
    country = models.CharField(max_length=75, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country


class Expertise(models.Model):
    expertise_code = models.CharField(max_length=20, unique=True)
    expertise_desc = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Expertise'

    def __str__(self):
        return self.expertise_code


class Speaker(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=75, null=False)
    state = models.CharField(max_length=2, null=False)
    zip = models.CharField(max_length=10, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    expertise = models.ForeignKey(Expertise, null=False, on_delete=models.CASCADE)
    credentials = models.TextField(null=False)
    bio = models.TextField(null=False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return self.last_name + "," + self.first_name


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250, null=False)
    web_address = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=75, null=False)
    state = models.CharField(max_length=2, null=False)
    zip = models.CharField(max_length=10, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    bio = models.TextField(null=False)
    logo = models.ImageField()
    active = models.BooleanField()


class Event(models.Model):
    event_name = models.CharField(max_length=150, null=False)
    event_tag = models.CharField(max_length=250, null=False)
    event_start_date = models.DateField(null=False)
    event_end_date = models.DateField(null=False)
    event_location = models.CharField(max_length=150, null=False)
    event_venue = models.CharField(max_length=150, null=False)
    venue_details = models.TextField(null=False)
    venue_location = models.TextField(null=False)
    venue_directions = models.TextField(null=False)
    accomodations = models.TextField(null=False)
    active = models.BooleanField()
    speakers = models.ManyToManyField(Speaker)
    sponsors = models.ManyToManyField(Sponsor)


class EventOffer(models.Model):
    offer_title = models.CharField(max_length=250, null=False)
    offer_subtitle = models.CharField(max_length=250, null=True)
    offer_details = models.TextField(null=False)
    event = models.ManyToManyField(Event)
    active = models.BooleanField()


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    guest = models.BooleanField()
    guest_first_name = models.CharField(max_length=100, null=True)
    guest_last_name = models.CharField(max_length=100, null=True)
