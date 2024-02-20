from django.shortcuts import render
from enroll.forms import stuform
# Create your views here.
def student_form(request):
    if request.method == 'POST':
        sf = stuform(request.POST)
        if sf.is_valid():
            name = sf.cleaned_data['name']
            email = sf.cleaned_data['email']
            print('Name : ',name)
            print('Email : ',email)
    else:
        sf = stuform()
    return render(request,'enroll/student_form.html',{'sf':sf})
