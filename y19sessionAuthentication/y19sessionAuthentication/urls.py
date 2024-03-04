
# from django.contrib import admin
# from django.urls import path
# from api import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# #     path('LCStudent/',views.LCStudentApi.as_view()),
# #     path('RUDStudent/<int:pk>',views.RUDStudentApi.as_view()),
#     path('studentapi/',views.StudentListCreate.as_view()),
#     path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
# ]

from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    
]



