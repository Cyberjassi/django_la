from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_python(request):
    detail = {'name':'jay','course':'python'}
    return render(request,'course/courseone.html',detail)
def learn_django(request):
    detail = {'name':'ashsih','course':'django'}
    return render(request,'course/coursetwo.html',detail)

