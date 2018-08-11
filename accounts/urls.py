from django.urls import path
from . forms import LoginForm
from . import views
from django.contrib.auth.views import (
    login,
)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('s/', views.LoginRedirect.as_view(), name='login_redirect'),
    path('login/', login, {'authentication_form': LoginForm}, name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('aboutus/', views.AboutView.as_view(), name='about'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:id>/', views.NewsDetailView.as_view(), name='detail'),
    path('<int:id>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:id>/edit/', views.UpdateView.as_view(), name='update'),
    path('<int:id>/confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('<int:id>/confirm_edit/', views.ConfirmEdit.as_view(),
         name='confirm_edit'),
]
