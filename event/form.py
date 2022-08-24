from django import forms
from .models import EventRegistration
from django.forms import modelformset_factory


class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event',
                  'member']
        widgets = {
           'event': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'event',
                                           'placeholder': '...'}),
           'member': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'member',
                                            'placeholder': '...'})
        }


GuestFormSet = modelformset_factory(
    EventRegistration, fields=("guest_name", "guest_Email"), extra=1
)

