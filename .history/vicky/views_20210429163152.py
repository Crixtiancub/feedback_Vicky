from django.shortcuts import render, redirect
import os
from modelo_IA.archivos_Python.pipeline import Pipeline
from vicky import templates
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)

    if num_visits == 0:
        request.session['num_visits'] = 3
        return redirect(noVisitas)
    else:
        request.session['num_visits'] = num_visits - 1

        contexto = {
            'num_visits': num_visits,
        }    

        return render(request, 'respuesta_Vicky.html' , {'visitas':contexto})

def noVisitas(request):
    return render(request, 'noVisitas.html')

def respuesta_Vicky(request):
    pregunta = request.GET('pregunta_Vicky')
    respuesta = model.run_model(pregunta)
    return render(request, 'noVisitas.html')