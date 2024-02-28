from django.shortcuts import render
from enroll.forms import StudentRegister
from enroll.models import Stu

# Create your views here.
def show(request):
    
    
    if request.method == 'POST':
        sf = StudentRegister(request.POST)
        if sf.is_valid():
            nm = sf.cleaned_data['name']
            em = sf.cleaned_data['email']
            pw = sf.cleaned_data['password']

            reg = Stu(name=nm,email=em,password=pw)
            reg.save()
            sf = StudentRegister()
    else:
        sf = StudentRegister()
    d1 = Stu.objects.all().filter(name='jay')
    
    return render(request,'enroll/db.html',{'st':sf,'data':d1})


