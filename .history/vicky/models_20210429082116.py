from django.db import models

# Create your models here.

class preguntas_Vicky(models.Model):
    pregunta = models.TextField(max_length=100)
    acierto = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1)])