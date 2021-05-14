from django.urls import path
from . import views
from django.conf.urls import url


# Direccionamiento de las paginas
urlpatterns = [
    path(r'', views.home, name="home"),
]
