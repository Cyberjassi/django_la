from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_python(request):
    return HttpResponse(200)
def fees_dejango(request):
    return HttpResponse(300)
