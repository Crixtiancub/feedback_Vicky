from django.shortcuts import render


from vicky import templates
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)
    request.session['num_visits'] = num_visits - 1

    if num_visits == 0:
        request.session['num_visits'] = 3
        noVisitas(request)

    contexto = {
        'num_visits': num_visits
    }    

    return render(request, 'dashboard.html' , {'visitas':contexto})

def noVisitas(request):
    return render(request, 'noVisitas.html')