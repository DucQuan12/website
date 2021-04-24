from django.contrib import admin
# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import MyUser


class Post(ModelAdmin):
    list_display = ['user', 'email']

admin.site.register(MyUser)