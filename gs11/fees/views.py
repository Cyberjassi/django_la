from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_python(request):
    detail = {'course':'Python hero to zero','fees':12000}
    return render(request,'fees/feespy.html',detail)
def fees_django(request):
    detail = {'course':'Django hero to zero','fees':15000}
    return render(request,'fees/feesdj.html',detail)