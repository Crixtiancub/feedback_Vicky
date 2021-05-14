from django.urls import path
from . import views


# Direccionamiento de las paginas
urlpatterns = [
    path(r'vicky/', views.home, name='vicky'),
    path(r'noVisitas/', views.noVisitas, name="noVisitas"),
    path(r'', views.user_Name, name='user_Name')
]
