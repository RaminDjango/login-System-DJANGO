from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('registru/', views.registrare, name='registrare-url'),
    path('login/', views.logare, name='logins-url'),
    path('logout/', views.logut, name='log-out'),
    path('message/', views.msg, name='mesaji'),
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='reset_password.html')
         , name='reset_password'),
    path('reset_password_send/', 
         auth_views.PasswordResetDoneView.as_view(template_name='reset_password_send.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), 
         name='password_reset_complete'),
    
]