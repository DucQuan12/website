from django.urls import path
from User import views
from django import urls
from django.contrib.auth import views as core_views
from django.conf.urls import url


app_name = 'User'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.singup.as_view(), name='signup'),
    path('login/', views.login1.as_view(), name='login'),
    path('logout/', core_views.auth_logout, {'next_page': '/user/login/'}, name='logout'),
    path('activate/<uidbase64>/<token>/', views.activate, name='activate'),
    path('account_active_sent/', views.account_active_sent, name='account_active_sent'),
]