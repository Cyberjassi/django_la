from django import forms
from django.core import validators
from .models import User

class stuform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email']
        labels = {
            'name': 'Enter name',
            'passwordk': 'Enter Password',
            'email': 'Enter Email'
        }
        error_messages = {
            'name': {'required': 'Naam likh'}
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }
