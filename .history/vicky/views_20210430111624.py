from django.shortcuts import render, redirect
import os
from modelo_IA.archivos_Python.pipeline import Pipeline
from vicky import templates

from forms import ContactForm

model = Pipeline()
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)

    if num_visits == 0:
        request.session['num_visits'] = 3
        return redirect(noVisitas)
    else:
        request.session['num_visits'] = num_visits - 1

        form = ContactForm(request.POST)

        if form.is_valid():
            pregunta = str(form.clean_data['retorno_Pregunta'])
            respuesta = str(form.clean_data['retorno_Respuesta'])
            
            if 'Si' in request.POST:
                acierto = 1
            if 'No' in request.POST:
                acierto = 0 

            contexto = {
                'pregunta': pregunta,
                'respueta': respuesta,
                'acierto': acierto,
                'num_visits': num_visits,
            }    

            return render(request, 'dashboard.html' , contexto)

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