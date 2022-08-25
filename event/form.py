from django import forms
from .models import EventRegistration, Guest
from django.forms import modelformset_factory


class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event',
                  'member',
                  'attendance']


GuestFormSet = modelformset_factory(
    Guest, fields=("guest_name", "guest_email", "attendance"), extra=1
)

