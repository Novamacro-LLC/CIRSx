from django import forms
from .models import Communication


class ContactForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ['first_name',
                  'last_name',
                  'email',
                  'subject',
                  'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'id': 'firstName',
                                                 'placeholder': ''}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'lastName',
                                                'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': 'name@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'subject',
                                              'placeholder': ''}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'placeholder': ''})
        }

