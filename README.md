# Ex02 Django ORM Web Application
## Date: 21/10/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)
```

## OUTPUT
![Alt text](football.png)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
