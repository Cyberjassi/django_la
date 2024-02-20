from django import forms
from django.core import validators

class stuform(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(3)])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password (Again)', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_dta = super().clean()
        p = cleaned_dta.get('password')
        pr = cleaned_dta.get('rpassword')
        
        if p != pr:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_dta
