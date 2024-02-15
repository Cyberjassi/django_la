from django.urls import path
from . import views
urlpatterns = [
    path('feespy/',views.fees_python,),
    path('feesdj/',views.fees_django),
]
