from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, News

# Dono models ko register karo takki wo admin panel mein dikhein
admin.site.register(Student)
admin.site.register(News)