from django import forms
from .models import EventRegistration, Marks


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

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks

        fields = ['guest_name',
                  'guest_email',
                  'attendance'
        ]

        widgets = {
            'guest_name': forms.TextInput(attrs={'class': 'formset-field'}),
            'guest_email': forms.TextInput(attrs={'class': 'formset-field'}),
            'attendance': forms.TextInput(attrs={'class': 'formset-field'})
        }