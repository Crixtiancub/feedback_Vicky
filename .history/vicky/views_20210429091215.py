from django.shortcuts import render


from vicky import templates
# Create your views here.

num_visits = request.session.get('num_visits', 3)

def home(request):

    contexto = {
        'num_visits': num_visits
    }    

    return render(request, 'dashboard.html' , {'visitas':contexto})