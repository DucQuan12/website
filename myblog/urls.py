from django.urls import path
from myblog import views

app_name = 'myblog'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('add', views.add_content.as_view(), name='add'),
    path('view', views.view, name='view'),
]
