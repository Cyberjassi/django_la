from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'enroll/home.html')
def show_details(request,my_id):
    if my_id == 1:
        student = {'id':my_id,'name':'Rohan1'}
    if my_id == 2:
        student = {'id':my_id,'name':'jay2'}
    if my_id == 3:
        student = {'id':my_id,'name':'shri3'}
    # student = {'id':my_id}
    return render(request,'enroll/show.html',student)
