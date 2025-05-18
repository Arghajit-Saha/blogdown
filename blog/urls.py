from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('create/', views.create, name='create'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.showPage, name='page'),
]
