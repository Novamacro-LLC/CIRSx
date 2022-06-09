from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=25, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'id': 'firstName',
                                                               'placeholder': ''}))
    last_name = forms.CharField(max_length=25, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'id': 'lastName',
                                                              'placeholder': ''}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'id':'email',
                                                                           'palceholder': 'name@example.com'}))
    subject = forms.CharField(max_length=150, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'id': 'subject',
                                                            'placeholder': ''}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                          'id': 'message',
                                                                          'placeholder': ''}))
