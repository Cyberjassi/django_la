# # from django.shortcuts import render
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response

# # # @api_view()
# # # def hello_world(request):
# # #     return Response({'msg':'Hello World!'})

# # # @api_view(['POST'])
# # # def hello_world(request):
# # #     if request.method == "POST":
# # #         print(request.data)
# # #         return Response({'msg':'This is Post Request'})
# # @api_view(['GET','POST'])
# # def hello_world(request):
# #     if request.method == 'GET':
# #         return Response({'msg':'This is Get Request'})
# #     if request.method == "POST":
# #         print(request.data)
# #         return Response({'msg':'This is Post Request','data':request.data})

# # from django.shortcuts import render
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import Student
# # from .serializers import StudentSerializer

# # @api_view(['GET','POST','PUT','DELETE'])
# # def student_api(request,pk=None):
# #     if request.method == 'GET':
# #         id = request.data.get('id')
# #         if id is not None:
# #             stu = Student.objects.get(id=id)
# #             serializer = StudentSerializer(stu)
# #             return Response(serializer.data)
# #         stu = Student.objects.all()
# #         serializer = StudentSerializer(stu, many = True)
# #         return Response(serializer.data)
    
# #     if request.method == 'POST':
# #         serializer = StudentSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response({'msg':'Data Created'})
# #         return Response(serializer.errors)  
        
# #     if request.method == 'PUT':
# #         id = request.data.get('id')
# #         stu = Student.objects.get(pk=id)
# #         serializer = StudentSerializer(stu,data= request.data,partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response({'msg':'Your Data has Been updated'})
# #         return Response(serializer.errors)
    
# #     if request.method == 'DELETE':
# #         id = request.data.get('id')
# #         stu = Student.objects.get(pk=id)
# #         stu.delete()
# #         return Response({"msg":"Successful Delted"})


# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request,pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
#     if request.method == 'PUT':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Your Data has Been updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data= request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data has Been updated'})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"msg":"Successful Delted"})

# class base api view--
# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework.views import APIView

# class student_api(APIView):
#     def get(self,request,pk=None,format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     def post(self,request,format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data is inserted'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk= id)
#         serializer = StudentSerializer(stu,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data is updated'},status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def patch(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk= id)
#         serializer = StudentSerializer(stu,data = request.data,partial =True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data is updated'},status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self , request,pk):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response({'msg':'Data Deleted Successfully!!'},status=status.HTTP_200_OK)

# Genericapiview and model mixin-
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin

# class LCStudentApi(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)



# class RUDStudentApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
# # class StudentList(GenericAPIView,UpdateModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # class StudentList(GenericAPIView,DestroyModelMixin):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer


# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

# # class StudentList(ListAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework import viewsets

# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#     def create(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_201_CREATED)
#     def update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Update Data Successfully!!'})
#         return Response(serializer.errors)
#     def partial_update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Update Data Successfully!!'})
#         return Response(serializer.errors)
#     def destroy(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk = id)
#         stu.delete()
#         return Response({'msg':'Data Deleted!!'})
 
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import viewsets

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

from .models import Student
from django.contrib.auth import logout
from .serializers import StudentSerializer
from rest_framework import viewsets


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .coustompermission import MyPermission

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # permission_classes = [IsAuthenticatedOrReadOnly]
#     permission_classes = [DjangoModelPermissions]


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         logout(request)
#         return Response({"detail": "Successfully logged out."})

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [MyPermission]
