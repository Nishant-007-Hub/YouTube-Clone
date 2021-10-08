from django.urls import path
from .import views

app_name = "tube"
urlpatterns = [
    path('', views.home, name="home"),
    path('watch/<int:myid>', views.watch, name="watch"),
    path('search', views.search, name="search"),
]
