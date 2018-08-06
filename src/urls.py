from django.urls import path, include
from django.contrib import admin
from accounts import views
from accounts.views import IndexView



urlpatterns = [
	path('', IndexView.as_view(),name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
]
