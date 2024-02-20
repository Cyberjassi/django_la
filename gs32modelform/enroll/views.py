from django.shortcuts import render
from enroll.forms import stuform
from .models import User
# Create your views here.
def student_form(request):
    if request.method == 'POST':
        sf = stuform(request.POST)
        if sf.is_valid():
            nm = sf.cleaned_data['name']
            em = sf.cleaned_data['email']
            pw = sf.cleaned_data['password']
            # reg = User(name=nm,email=em,password=pw)
            reg = User(id = 1,name=nm,email=em,password=pw)
            reg.save()

    else:
        sf = stuform()
    return render(request,'enroll/student_form.html',{'sf':sf})
