from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def learn_python(request):
    names = {'name':'Rahul','roll':102}
    return render(request,'course/coursepy.html',names)
def learn_django(request):
    names = {'name':'Rahul','roll':102}
    return render(request,'course/coursepy.html',names)