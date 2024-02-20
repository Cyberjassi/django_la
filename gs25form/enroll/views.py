from django.shortcuts import render
from enroll.forms import stuform
# Create your views here.
def student_form(request):
    sf = stuform(auto_id='jhsdf',initial={'name':'jay'})
    return render(request,'enroll/student_form.html',{'sf':sf})
