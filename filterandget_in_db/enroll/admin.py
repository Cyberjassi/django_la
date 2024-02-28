from django.contrib import admin
from .models import Stu

@admin.register(Stu)
class SuAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']