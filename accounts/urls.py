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
	path('create/', views.create, name='create'),
	path('aboutus/', views.about, name='about'),
	path('profile/', views.profile, name='profile'),   
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.update, name='update'),

]
