"""
serach fields symbols - 
^ - Start wotj
= - Exact matches
@ - Full text search
$ - Regex search

if we need search through the link then we write search =  but if we need to change it then setting.py-
REST_FRAMEWORK={
'SEARCH_PARAM':'name'
}

"""

from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
  

# for serching filter 
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    filter_backends = [SearchFilter]
    # search_fields = ['city']

# it return name start with letter
    search_fields = ['^name']
    #or we have different symbol


