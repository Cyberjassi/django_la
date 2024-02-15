from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def learn_python(request):
    names = {'names':['A','B','C','D']}
    return render(request,'course/coursepy.html',names)
def learn_django(request):
    names = {'names':['rahul','ravi','rohan']}
    return render(request,'course/coursedj.html',names)