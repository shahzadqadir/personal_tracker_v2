from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('track/', include('track.urls')),
    path('timetable/', include('timetable.urls')),
    path('api/v1/', include('api.urls')),
    path('authenticate/', obtain_auth_token, name="obtain_auth_token"),
]
