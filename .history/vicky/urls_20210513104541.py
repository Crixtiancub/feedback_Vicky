from django.urls import path
from . import views


# Direccionamiento de las paginas
urlpatterns = [
    path(r'vicky/', views.home, name='vicky'),
    path(r'noVisitas/', views.noVisitas, name="noVisitas"),
    path(r'', views.respuesta_Vicky, name='user_Name')
]
