from . import views
from django.urls import path

urlpatterns = [
    path('', views.admin_login, name='adminlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
