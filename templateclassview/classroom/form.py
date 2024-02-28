from django import forms

class f1(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=60)