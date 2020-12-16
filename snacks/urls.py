from django.urls import path

from .views import HomePage

from .views import AboutPage

urlpatterns = [
  path('', HomePage.as_view(), name="home"),
  path('about/', AboutPage.as_view(), name="about"),
]