from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_python(request):
    detail = {'course':'python','fees':2000}
    return render(request,'fees/feesone.html',detail)
def fees_django(request):
    detail = {'course':'django','fees':5000}
    return render(request,'fees/feestwo.html',detail)
