from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse 
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    print("I am View")
    return HttpResponse("This is Home Page")

def excep(request):
    print("I am Excp View")
    a = 10/0
    return HttpResponse("This is Excep Page")

def user_info(request):
    print("I am User info View")
    context = {'name':'Rahul'}
    return TemplateResponse(request,'blog/user.html',context)

