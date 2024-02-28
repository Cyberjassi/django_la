from django.shortcuts import render

# Create your views here.
# def setcookie(request):
#     response = render(request,'student/setcookie.html')
#     response.set_cookie('name','jay',max_age=10)
#     return response

# def getcookie(request):
#     # name = request.COOKIES['name']
#     name = request.COOKIES.get('name')
#     return render(request,'student/getcookie.html',{'name':name})

# def delcookie(request):
#     response = render(request,'student/delcookie.html')
#     response.delete_cookie('name')
#     return response

def setsession(request):
    request.session['name'] = 'jay'
    return render(request,'student/setsession.html')

def getsession(request):
    # name = request.session.get('name')
    # keys = request.session.keys()
    # items = request.session.items()
    # age = request.session.setdefault('age','26')
    # return render(request,'student/getsession.html',{'name':name,'keys':keys})

    name = request.session['name']
    request.session.set_expiry(100)
    return render(request,'student/getsession.html',{'name':name})

def delsession(request): 
    request.session.flush()
    request.session.clear_expired()   #use for clear all expire session in db
    # if 'name' in request.session:
    #     del request.session['name']
    return render(request,'student/delsession.html')