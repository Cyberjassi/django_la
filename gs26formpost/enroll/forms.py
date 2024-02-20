from django import forms
class stuform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
   

    