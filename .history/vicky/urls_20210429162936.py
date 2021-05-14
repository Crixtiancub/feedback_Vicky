from django.urls import path
from . import views


# Direccionamiento de las paginas
urlpatterns = [
    path(r'', views.home, name="home"),
    path(r'noVisitas/', views.noVisitas, name="noVisitas"),
    path(r'respuesta_Vicky/', views.respuesta_Vicky, name='respuesta_Vicky')
]
