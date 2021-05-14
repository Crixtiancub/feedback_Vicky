from django.shortcuts import render, redirect
import os
from modelo_IA.archivos_Python.pipeline import Pipeline
from vicky import templates
model = Pipeline()
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)

    if num_visits == 0:
        request.session['num_visits'] = 3
        return redirect(noVisitas)
    else:
        request.session['num_visits'] = num_visits - 1

        if request.method=='POST' and 'Si' in request.POST:
            pregunta = str(request.POST['pregunta_Vicky'])
            respuesta = str(request.POST['respuesta_Vicky'])
            acierto = 1

            contexto = {
                'pregunta': pregunta,
                'respueta': respuesta,
                'acierto': acierto,
                'num_visits': num_visits,
            }    
            return render(request, 'dashboard.html' , contexto)

        if request.method=='POST' and 'No' in request.POST:
            pregunta = str(request.POST['pregunta_Vicky'])
            respuesta = str(request.POST['respuesta_Vicky'])
            acierto = 0

            contexto = {
                'pregunta': pregunta,
                'respueta': respuesta,
                'acierto': acierto,
                'num_visits': num_visits,
            }     
            return render(request, 'dashboard.html' , contexto)

    return render(request, 'dashboard.html')


def noVisitas(request):
    return render(request, 'noVisitas.html')

def respuesta_Vicky(request):
    pregunta = str(request.GET['pregunta_Vicky'])
    respuesta = model.run_model(pregunta)
    context = {
        "pregunta":pregunta,
        "respuesta":respuesta
    }
    return render(request, 'respuesta_Vicky.html', context)