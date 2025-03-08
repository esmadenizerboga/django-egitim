from django.urls import path 
from . import views 

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home 
# http://127.0.0.1:8000/moviess
# http://127.0.0.1:8000/moviess/3
# http://127.0.0.1:8000/movies/walking-dead

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("moviess", views.moviess, name="moviess"),
    path("moviess/<int:id>", views.moviedetails, name="details"),
]
