from django.shortcuts import render
from enroll.models import Student

def student(request):
    # stud = Student.objects.all()
    stud = Student.objects.get(pk=1)
    return render(request,'enroll/studetail.html',{'stu':stud})

# Create your views here.
