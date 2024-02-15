from django.urls import path
from . import views
urlpatterns = [
    path('learnpy/',views.Course),
]
