from . import views
from django.urls import path

urlpatterns = [
    path('', views.admin_login, name='adminlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs_admin, name='blogs'),
    path('contact/', views.contact, name='contact-admin'),
    path('contact/<int:id>/delete/', views.contact_delete, name='contact_delete'),
    path('blogs/<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
    path('users/<str:username>/delete/', views.user_delete, name='user_delete')
]
