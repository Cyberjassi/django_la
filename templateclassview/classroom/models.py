from django.db import models

# Create your models here.
class Stu(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}, email is {self.email} and password {self.password}"
