from django.urls import path
from . import views


# Direccionamiento de las paginas
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'noVisitas/', views.noVisitas, name="noVisitas"),
    path(r'user_Name/', views.respuesta_Vicky, name='user_Name')
]
