from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_python(request):
    detail = {'name':'Jay','course':'Python hero to zero'}
    return render(request,'course/coursepy.html',detail)
def learn_django(request):
    detail = {'name':'sham','course':'Django hero to zero'}
    return render(request,'course/coursedj.html',detail)