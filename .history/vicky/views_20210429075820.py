from django.shortcuts import render


from vicky import templates
# Create your views here.


def home(request):
    return render(request, 'dashboard.html')