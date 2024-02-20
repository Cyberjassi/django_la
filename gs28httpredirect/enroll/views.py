from django.shortcuts import render
from enroll.forms import stuform
from django.http import HttpResponseRedirect
# Create your views here.
def thankyou(request):
    return render(request,'enroll/thank.html')
def student_form(request):
    if request.method == 'POST':
        sf = stuform(request.POST)
        if sf.is_valid():
            name = sf.cleaned_data['name']
            email = sf.cleaned_data['email']
            print('Name : ',name)
            print('Email : ',email)
            return HttpResponseRedirect('/form/success')
            # return render(request,'enroll/thank.html',{'name':name})
    else:
        sf = stuform()
    return render(request,'enroll/student_form.html',{'sf':sf})
