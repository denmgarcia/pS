from django.urls import path

from . import views
from django.contrib.auth.views import (
    login,
    logout
)

urlpatterns = [
    path('', views.home),
    path('s/', views.login_redirect, name='login_redirect'),
    path('login/',login, {'template_name': 'accounts/login.html'}),
    path('logout/',logout, {'template_name': 'accounts/logout.html'}),
    path('register/', views.register, name='register'),

]
