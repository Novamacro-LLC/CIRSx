from django import forms
from .models import EventRegistration


class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event',
                  'member',
                  'guest',
                  'guest_name',
                  'guest_email']
        widgets = {
           'event': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'event',
                                           'placeholder': '...'}),
           'member': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'member',
                                            'placeholder': '...'}),
           'guest': forms.BooleanField(),
           'guest_name': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'guest_name',
                                                'placeholder': '...'}),
           'guest_email': forms.EmailInput(attrs={'class': 'form-control',
                                                  'id': 'guest_email',
                                                  'placeholder': '...'})
        }