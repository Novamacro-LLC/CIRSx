from django.db import models
from django.forms.models import inlineformset_factory
from account.models import Account, Country


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
    phone = models.CharField(max_length=10, null=False, default='000-000-0000')
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    expertise = models.ForeignKey(Expertise, null=False, on_delete=models.CASCADE)
    credentials = models.TextField()
    bio = models.TextField()
    image = models.ImageField(upload_to='speaker/', height_field=None, width_field=None, max_length=100,
                              default='Transparent-gold.jpg')
    active = models.BooleanField(default=True)

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
    logo = models.ImageField(upload_to='sponsor/', height_field=None, width_field=None,
                             default='Transparent-gold.jpg')
    active = models.BooleanField()

    def __str__(self):
        return self.sponsor_name


class EventType(models.Model):
    event_type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.event_type


class Event(models.Model):
    event_name = models.CharField(max_length=150, null=False, unique=True)
    event_tag = models.CharField(max_length=250, null=False)
    event_start_date = models.DateField(null=False)
    event_end_date = models.DateField(null=True)
    event_start_time = models.TimeField(null=True)
    event_end_time = models.TimeField(null=True)
    event_location = models.CharField(max_length=150, null=False)
    event_venue = models.CharField(max_length=150, null=False)
    venue_image = models.ImageField(upload_to='event/', height_field=None, width_field=None,
                                    default='Transparent-gold.jpg')
    venue_details = models.TextField(null=False)
    venue_location = models.TextField(null=False)
    venue_directions = models.TextField(null=False)
    accomodations = models.TextField(null=False)
    active = models.BooleanField()
    header_image = models.ImageField(upload_to='event/', height_field=None, width_field=None,
                                     default='Transparent-gold.jpg')
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    speakers = models.ManyToManyField(Speaker)
    sponsors = models.ManyToManyField(Sponsor)

    def __str__(self):
        return self.event_name


class EventOffer(models.Model):
    offer_title = models.CharField(max_length=250, null=False)
    offer_subtitle = models.CharField(max_length=250, null=True)
    offer_details = models.TextField(null=False)
    event = models.ManyToManyField(Event)
    active = models.BooleanField()


class EventAttendance (models.Model):
    attendance = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.attendance


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    attendance = models.ForeignKey(EventAttendance, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.event

    class Meta:
        db_table = "eventregistration"


class Guest(models.Model):
    guest_name = models.CharField(max_length=100, null=True)
    guest_email = models.EmailField(max_length=100, null=True)
    attendance = models.ForeignKey(EventAttendance, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.guest_name

    class Meta:
        db_table = "event_guest"