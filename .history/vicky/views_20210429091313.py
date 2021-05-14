from django.shortcuts import render


from vicky import templates
# Create your views here.

def home(request):

    num_visits = request.session.get('num_visits', 3)

    contexto = {
        'num_visits': num_visits
    }    

    return render(request, 'dashboard.html' , {'visitas':contexto})