from django import forms
from .models import EventRegistration


class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event',
                  'member',
                  'guest',
                  'guest_last_name',
                  'guest_first_name']
        widgets = {
           'event': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'event',
                                           'placeholder': '...'}),
           'member': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'member',
                                            'placeholder': '...'}),
           'guest': forms.BooleanField(),
           'guest_first_name': forms.TextInput(attrs={'class': 'form-control',
                                                      'id': 'guest_first_name',
                                                      'placeholder': '...'}),
           'guest_last_name': forms.TextInput(attrs={'class': 'form-control',
                                                     'id': 'guest_last_name',
                                                     'placeholder': '...'})
        }