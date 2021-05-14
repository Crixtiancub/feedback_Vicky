from django.shortcuts import render, redirect
import os
from modelo_IA.archivos_Python.pipeline import Pipeline
from vicky import templates
from .models import *
from django.template.response import TemplateResponse

model = Pipeline()

# Create your views here.

def home(request):

    if request.GET:
        request.session['user_Name'] = str(request.GET.get('user_Name'))

        print(request.session['user_Name'])

        request.session['num_visits'] = 3

        contexto = {
            'num_visits': request.session['num_visits'],
        }        

        return render(request, 'dashboard.html', contexto)

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
                'num_visits': request.session['num_visits'],
            }

            if request.session['num_visits'] == 0:

                request.session['num_visits'] = 3

                return redirect('../noVisitas')  

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
                'num_visits': request.session['num_visits'],
            }

            print(context)

            if request.session['num_visits'] == 0:

                request.session['num_visits'] = 3

                return redirect('../noVisitas')  

            return TemplateResponse(request, 'dashboard.html' , context)

        
        pregunta = str(request.POST.get('pregunta_Vicky'))
        respuesta = model.run_model(pregunta, user_name= request.session['user_Name'])

        context = {
            "pregunta":pregunta,
            "respuesta":respuesta,
            'num_visits': request.session['num_visits'],
        }

        print(context)

        return TemplateResponse(request, 'dashboard.html' , context)

    else:
       
        contexto = {
            'num_visits': request.session['num_visits'],
        }        

        return render(request, 'dashboard.html', contexto)

def noVisitas(request):

    nombre_Usuario = str(request.session['user_Name'])
    comentario_Usuario = str(request.POST.get('comentario'))

    user = usuario(
        usuario = nombre_Usuario,
        comentario = comentario_Usuario
    )

    user.save()

    print(request.session['user_Name'])

    return render(request, 'noVisitas.html')

def user_Name(request):

    return render(request, 'user_Name.html')