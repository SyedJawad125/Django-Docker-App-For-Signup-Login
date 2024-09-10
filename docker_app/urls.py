from django.urls import path
from docker_app import views


urlpatterns = [
  path("", views.home, name="home"),  # Matches the root URL and calls the home view
#   path("about-us/", views.about_us, name="about_us"),  # Matches the about-us URL and calls the about_us view
]