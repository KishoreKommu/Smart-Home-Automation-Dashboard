from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('dashboard/', views.dashboard_view, name='dashboard'),  
    path('toggle/<int:device_id>/', views.toggle_device, name='toggle_device'),
    path('delete/<int:device_id>/', views.delete_device, name='delete_device'),
    path('add_device/', views.add_device, name='add_device'),
    path('about/', views.about_view, name='about'),
     path('login/', views.login_view, name='login'),
     path('register/', views.register_view, name='register'),


]



