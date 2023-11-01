from django.db import models
from django.contrib import admin
class Football (models.Model):
    level=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    email=models.EmailField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('level','name','date_of_birth','age','email')