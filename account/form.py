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


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid email or password')
