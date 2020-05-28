from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('register/employee_registration/', views.employee_registration, name='employee_registration'),
    path('login/', views.login, name='login'),
]
