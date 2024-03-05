from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  

    # userd for overide queryset -
    def get_queryset(self):
        #it means which user send request
        user = self.request.user
        #it means show that data of particular user-
        return Student.objects.filter(passby=user)