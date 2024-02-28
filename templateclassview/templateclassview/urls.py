"""
URL configuration for templateclassview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from classroom.views import homepage,formview,Thankyouview,StuCreateView,StuListView,StuDetailVies,StuUpdateView,StuDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage.as_view(),name = 'home'),
    path('form/',formview.as_view(),name = 'form'),
   
    path('thanks/',Thankyouview.as_view()),
    path('create/',StuCreateView.as_view(),name='create'),
    path('list_stu/',StuListView.as_view(),name='list'),
    path('stu_detail/<int:pk>',StuDetailVies.as_view(),name='detail_stu'),
    path('update_stu/<int:pk>',StuUpdateView.as_view(),name='update_teacher'),
    path('delete_stu/<int:pk>/',StuDeleteView.as_view(),name = 'delete')
]
