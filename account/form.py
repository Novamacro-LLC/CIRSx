from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Required, add a valid email address')

    class Meta:
        model = Account
        fields = ('email',
                  'username',
                  'first_name',
                  'last_name',
                  'address',
                  'city',
                  'state',
                  'post_code',
                  'phone',
                  'country',
                  'password1',
                  'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'placeholder': '...'}),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'id': 'username',
                                               'placeholder': '...'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'id': 'first_name',
                                                 'placeholder': '...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'last_name',
                                                'placeholder': '...'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'last_name',
                                              'placeholder': '...'}),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                           'id': 'last_name',
                                           'placeholder': '...'}),
            'state': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'last_name',
                                            'placeholder': '...'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'last_name',
                                                'placeholder': '...`'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'last_name',
                                            'placeholder': '...'}),
            'country': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'last_name',
                                              'placeholder': '...'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'id': 'last_name',
                                                    'placeholder': '...'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'id': 'last_name',
                                                    'placeholder': '...'}),
        }


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid email or password')
