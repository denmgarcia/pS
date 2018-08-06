from django.urls import path
from . forms import LoginForm
from . import views
from django.contrib.auth.views import (
    login,
    logout
)
from .views import IndexView, NewsView,SearchView,RegisterView, ProfileView, CreateView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('s/', views.login_redirect, name='login_redirect'),
    path('login/',login, {'authentication_form':LoginForm}, name="login"),
    path('logout/',views.logout_views, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
	path('create/', views.CreateView.as_view(), name='create'),
	path('aboutus/', views.about, name='about'),
	path('profile/', views.ProfileView.as_view(), name='profile'), 
    path('search/', views.SearchView.as_view(), name='search'),  
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:id>/', views.news_detail, name='detail'),
    #path('users/', views.users),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.update, name='update'),
    path('<int:id>/confirm/', views.confirm, name='confirm'),
    path('<int:id>/confirm_edit/', views.confirm_edit, name='confirm_edit'),


    

]
