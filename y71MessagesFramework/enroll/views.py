from django.shortcuts import render
from .form import StudentRegistration

from django.contrib import messages
# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS,"your account has been created !!!")
            messages.info(request,"now you can login")
            print(messages.get_level(request))
            messages.debug(request,'This is Debug')
            # messages.success(request,'your account has been created')

    else:
        fm = StudentRegistration()
    return render(request,'enroll/registeration.html',{'form':fm})
