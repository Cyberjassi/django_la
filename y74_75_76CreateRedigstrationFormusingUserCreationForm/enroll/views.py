from django.shortcuts import render,HttpResponsePermanentRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm

from django.contrib.auth import login,authenticate,logout,update_session_auth_hash


def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Your registration Successfully!")  
            fm.save()
    else:
        fm = UserCreationForm()  # Moved outside of the else block
   
    return render(request, 'enroll/signup.html', {'form': fm})


def user_login(request):
    if request.user.is_authenticated:
        if not request.user.is_authenticated:
            if request.method == 'POST':
                fm = AuthenticationForm(data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    upass = fm.cleaned_data['password']
                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request, user) 
                        messages.success(request,'Login successfully!')
                        return HttpResponsePermanentRedirect('/profile/')
            else:
                fm = AuthenticationForm()
            return render(request, 'enroll/userlogin.html', {'form': fm})
        else:
            return HttpResponsePermanentRedirect('/profile/')
    else:
        return HttpResponsePermanentRedirect('/login/')


def user_profile(request):
    if request.user.is_authenticated:
        fm = UserChangeForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponsePermanentRedirect('/login/',{'name':request.user,'form':fm})

def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect('/login/')

# change password with old password
def user_change_pass(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponsePermanentRedirect('/profile/')
    else:
        fm = PasswordChangeForm(user=request.user) #kiska password change karna h wo argument me
    return render(request,'enroll/changepass.html',{'form':fm})

# change password without old password
def user_change_pass1(request):
    if request.method == "POST":
        fm = SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponsePermanentRedirect('/profile/')
    else:
        fm = SetPasswordForm(user=request.user) #kiska password change karna h wo argument me
    return render(request,'enroll/changepass1.html',{'form':fm})
