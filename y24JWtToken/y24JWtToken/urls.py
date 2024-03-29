from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter

#for token genration-
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView



router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
   
]

