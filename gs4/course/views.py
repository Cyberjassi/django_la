from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def django(request):
    return HttpResponse('This is django')
def python(request):
    return HttpResponse('This is python')