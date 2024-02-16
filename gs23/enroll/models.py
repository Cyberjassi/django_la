from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key = True)
    stuname = models.CharField(max_length = 70)
    stuid = models.IntegerField()
    stupass = models.CharField(max_length = 50)

 
