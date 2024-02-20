from django import forms
class stuform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 4:
    #         raise forms.ValidationError("Your length is less than 4")
    #     return valname
    def clean(self):
        cleaned_d = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname)<4:
            raise forms.ValidationError('Name length should be greater than 4')
        if len(valemail)<4:
            raise forms.ValidationError('Email length should be greater than 4')
    
   

    