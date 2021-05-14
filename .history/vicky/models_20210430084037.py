from django.db import models

# Create your models here.

class preguntas_Vicky(models.Model):
    pregunta = models.TextField(max_length=100)
    respuesta = models.TextField(max_length=200)
    acierto = models.PositiveIntegerField(default=1)