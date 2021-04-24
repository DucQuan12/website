from django.contrib import admin
from .models import blog
# Register your models here.

class Post(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']
admin.site.register(blog, Post)