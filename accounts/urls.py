from django.urls import path
from . forms import LoginForm
from . import views
from django.contrib.auth.views import (
    login,
    logout
)

urlpatterns = [
    path('', views.index),
    path('s/', views.login_redirect, name='login_redirect'),
    path('login/',login, {'authentication_form':LoginForm}, name="login"),
    path('logout/',views.logout_views, name='logout'),
    path('register/', views.register, name='register'),
	path('create/', views.create, name='create'),
	path('aboutus/', views.about, name='about'),
	path('profile/', views.profile, name='profile'), 
    path('search/', views.search, name='search'),  
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.news_detail, name='detail'),
    
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.update, name='update'),

]
