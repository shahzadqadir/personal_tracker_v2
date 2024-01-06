from django.urls import path

from pages.views import HomePageView, homepage

urlpatterns = [
    path('', homepage, name="homepage"),
]