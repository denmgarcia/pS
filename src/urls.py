from django.urls import path, include
from django.contrib import admin
from accounts import views


urlpatterns = [
	path('', views.index,name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('address_book/', include('address_book.urls')),
]
