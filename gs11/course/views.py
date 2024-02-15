from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def learn_python(request):
    d = datetime.now()
    detail = {'name':'Jay','course':'Python hero to zero','dt':d}
    return render(request,'course/coursepy.html',detail)
def learn_django(request):
    return render(request,'course/coursedj.html',{'nm':True,'age':12})