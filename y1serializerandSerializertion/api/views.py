from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
# def student_detail(request,pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type = 'application/json')

def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    serializers = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type = 'application/json')