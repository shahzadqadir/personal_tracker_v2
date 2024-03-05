from django.urls import path

from pages.views import homepage




urlpatterns = [
    path('', homepage, name="homepage"),
]