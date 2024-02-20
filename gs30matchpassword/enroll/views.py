from django.shortcuts import render
from enroll.forms import stuform
from django.http import HttpResponseRedirect
# Create your views here.
def student_form(request):
    if request.method == 'POST':
        sf = stuform(request.POST)
        if sf.is_valid():
            name = sf.cleaned_data['name']

            print('Name : ',name)
    else:
        sf = stuform()
    return render(request,'enroll/student_form.html',{'sf':sf})
