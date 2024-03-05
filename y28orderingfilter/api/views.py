"""


"""

from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
  

# for orderring filter-
from rest_framework.filters import OrderingFilter



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # to initilize filter ordering
    filter_backends = [OrderingFilter]
    # it filter by particular field
    ordering_fields = ['name']

    # through link - link/?ordering - fieldname


