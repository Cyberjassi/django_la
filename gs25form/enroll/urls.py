from django.urls import path
from . import views
urlpatterns = [
    path('enroll/student_form/',views.student_form)
]
