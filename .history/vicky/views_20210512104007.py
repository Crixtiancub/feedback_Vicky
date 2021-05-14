from django.shortcuts import render, redirect
import os
from modelo_IA.archivos_Python.pipeline import Pipeline
from vicky import templates
from .models import *
from django.template.response import TemplateResponse

model = Pipeline()

# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)

    if num_visits == 0:
        request.session['num_visits'] = 3

        if 'Si' in request.POST:
            acierto = str(request.POST.get('Si'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))
        
            envio_Pregunta = preguntas_Vicky(
            pregunta=pregunta,
            respuesta=respuesta,
            acierto= acierto
            )

            envio_Pregunta.save()

            print("Pregunta Saved...")

            context = {
                'num_visits': num_visits,
            }

            return TemplateResponse(request, 'noVisitas.html')


        if 'No' in request.POST:
            acierto = str(request.POST.get('No'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))

            envio_Pregunta = preguntas_Vicky(
                pregunta=pregunta,
                respuesta=respuesta,
                acierto= acierto
                )

            envio_Pregunta.save()

            print("Pregunta Saved...")

            context = {
                'num_visits': num_visits,
            }

            return TemplateResponse(request, 'noVisitas.html')

        
        pregunta = str(request.POST.get('pregunta_Vicky'))
        respuesta = model.run_model(pregunta)

        context = {
            "pregunta":pregunta,
            "respuesta":respuesta,
            'num_visits': num_visits,
        }

        return TemplateResponse(request, 'dashboard.html' , context)


    if request.POST:

        if 'Si' in request.POST:

            request.session['num_visits'] -= 1

            acierto = str(request.POST.get('Si'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))
        
            envio_Pregunta = preguntas_Vicky(
            pregunta=pregunta,
            respuesta=respuesta,
            acierto= acierto
            )

            envio_Pregunta.save()

            print("Pregunta Saved...")

            context = {
                'num_visits': num_visits,
            }

            return TemplateResponse(request, 'dashboard.html' , context)


        if 'No' in request.POST:

            request.session['num_visits'] -= 1
            
            acierto = str(request.POST.get('No'))
            pregunta = str(request.POST.get('retorno_Pregunta'))
            respuesta = str(request.POST.get('retorno_Respuesta'))

            envio_Pregunta = preguntas_Vicky(
                pregunta=pregunta,
                respuesta=respuesta,
                acierto= acierto
                )

            envio_Pregunta.save()

            print("Pregunta Saved...")

            context = {
                'num_visits': num_visits,
            }

            print(context)

            return TemplateResponse(request, 'dashboard.html' , context)

        # pregunta = str(request.POST.get('retorno_Pregunta'))
        # respuesta = str(request.POST.get('retorno_Respuesta'))
        
        pregunta = str(request.POST.get('pregunta_Vicky'))
        respuesta = model.run_model(pregunta)

        context = {
            "pregunta":pregunta,
            "respuesta":respuesta,
            'num_visits': num_visits,
        }

        print(context)

        return TemplateResponse(request, 'dashboard.html' , context)

    else:
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