from django.urls import path, include
from django.contrib import admin
from accounts import views
from accounts.views import IndexView
from django.conf import settings



urlpatterns = [
	path('', IndexView.as_view(),name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
