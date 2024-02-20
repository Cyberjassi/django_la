from django import forms
from django.core import validators


class stuform(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(3)])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    