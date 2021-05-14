from django.shortcuts import render, redirect
import os
from modelo_IA.archivos_Python.pipeline import Pipeline
from vicky import templates
from .models import *
model = Pipeline()
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)

    if num_visits == 0:
        request.session['num_visits'] = 3

        pregunta = str(request.POST.get('retorno_Pregunta'))
        respuesta = str(request.POST.get('retorno_Respuesta'))
        
        if 'Si' in request.POST:
            acierto = str(request.POST.get('Si'))
        else:
            acierto = str(request.POST.get('No'))

        envio_Pregunta = preguntas_Vicky(
            pregunta=pregunta,
            respuesta=respuesta,
            acierto= acierto
            )
            
        envio_Pregunta.save()

        return redirect(noVisitas)

    if request.POST:
        request.session['num_visits'] = num_visits - 1

        pregunta = str(request.POST.get('retorno_Pregunta'))
        respuesta = str(request.POST.get('retorno_Respuesta'))
        
        if 'Si' in request.POST:
            acierto = str(request.POST.get('Si'))
        else:
            acierto = str(request.POST.get('No'))

        context = {
            'num_visits': num_visits,
        }
        envio_Pregunta = preguntas_Vicky(
            pregunta=pregunta,
            respuesta=respuesta,
            acierto= acierto
            )
        envio_Pregunta.save()

        return render(request, 'dashboard.html' , context)
    
    request.session['num_visits'] = num_visits - 1

    contexto = {
        'num_visits': num_visits,
    }        

    return render(request, 'dashboard.html', contexto)


def noVisitas(request):
    return render(request, 'noVisitas.html')

def respuesta_Vicky(request):
    pregunta = str(request.POST['pregunta_Vicky'])
    respuesta = model.run_model(pregunta)
    context = {
        "pregunta":pregunta,
        "respuesta":respuesta
    }
    return render(request, 'respuesta_Vicky.html', context)