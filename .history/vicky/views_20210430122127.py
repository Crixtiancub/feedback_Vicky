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

        if request.POST:
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))
            acierto = 0

            if 'Si' in request.POST:
                acierto = 1


            context = {
                'pregunta': pregunta,
                'respuesta': respuesta,
                'acierto': acierto,
                'num_visits': num_visits,
            }
            print(context)    

            return render(request, 'dashboard.html' , context)

    contexto = {
        'num_visits': num_visits,
    }        

    return render(request, 'dashboard.html', contexto)


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