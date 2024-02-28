from .models import Stu
from django import forms

class StudentRegister(forms.ModelForm):
    class Meta:
        model = Stu
        fields = ['name','email','password']
        labels = {
                'name':'Enter Your Name',
                'email':'Enter Your Email',
                'password':'Enter Your Password',
        }
      