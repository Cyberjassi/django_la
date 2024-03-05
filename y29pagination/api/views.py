"""

for globally apply pagination then we go setting.py
and for locallly we want to do something view -
and we can make sperate class

ans also we have limitoffsetpaginatrion

cursor pagination-
it give user cursor page in which only we have next and previous instead of page no.
"""

from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView

# import the pagination through cutom file
from .mypagination import MyPageNumberPagination
from .mypagination import MyLimitOffsetPagination


from .mypagination import MyCursorPagination


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # define pagination class
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination

    pagination_class = MyCursorPagination
