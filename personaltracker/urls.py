from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('track/', include('track.urls')),
    path('api/v1/', include('api.urls')),
]
