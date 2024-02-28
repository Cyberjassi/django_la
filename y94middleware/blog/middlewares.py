# def my_middleware(get_response):
#     print("ONe Time Initialization")
#     def my_function(request):
#         print("this is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function

# class MyMiddleware:
#     def __init__(self,get_response) -> None:
#         self.get_response = get_response
#         print("One Time Initialization")

#     def __call__(self,request):
#         print("This is before view")
#         response = self.get_response(request)
#         print("Thls is after view")
#         return response
from django.http import HttpResponse

# class FatherMiddleware:
#     def __init__(self,get_response) -> None:
#         self.get_response = get_response
#         print("One Time Initialization")

#     def __call__(self,request):
#         print("This is Father before view")
#         response = HttpResponse("stop herer")
#         print("Thls is Father after view")
#         return response
    

# class BrotherMiddleware:
#     def __init__(self,get_response) -> None:
#         self.get_response = get_response
#         print("One Time Initialization")

#     def __call__(self,request):
#         print("This is Brother before view")
#         response = self.get_response(request)
#         print("Thls is Brother after view")
#         return response
    
# class MotherMiddleware:
#     def __init__(self,get_response) -> None:
#         self.get_response = get_response
#         print("One Time Initialization")

#     def __call__(self,request):
#         print("This is Mother before view")
#         response = self.get_response(request)
#         print("Thls is Mother after view")
#         return response

# class MyProcessMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         response = self.get_response(request)
#         return response
    
#     def process_view(request,*args,**kwargs):
#         return HttpResponse("This is before view")

# class MyExceptionMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         response = self.get_response(request)
#         return response
    
#     def process_exception(self,request,exception):
#         msg = exception
#         return HttpResponse(msg)
    

class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self,request,response):
        print("Process Template Response From Middleware ")
        response.context_data['name'] = 'Sonam'
        return response