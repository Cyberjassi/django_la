# for globaly in setting .py-
# REST_FRAMEWORK = {
# 'DEFAULT_FILTER_BACKEND':['django_filters.rest_framework.DjangoFilterBackend']
# }
# and we user filterset_fields = ['column_Name']   -for filter field
from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView

# for locally for filter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #this field for where you want to appy filter in which column
    # filterset_fields = ['city']


#this is local but we dont want to write in setting .py
    # and we can pass multiple argument
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city']

# and for link test-
# link/?filterfield-value
  



    