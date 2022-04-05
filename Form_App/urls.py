from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('success', views.success, name='success'),
    path('token_send', views.token_send, name='token_send'),
    path('error', views.error, name='error'),
    path('verify/<auth_token>', views.verify, name='verify'),


]
