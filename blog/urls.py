from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('create/', views.create, name='create'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('<slug:slug>/', views.showPage, name='page'),
    path('<slug:slug>/edit/', views.edit_blog, name='edit_blog'),
    path('<slug:slug>/delete/', views.delete_blog, name='delete_blog'),
]
