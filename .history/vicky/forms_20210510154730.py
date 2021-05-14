from django.forms import ModelForm
from .models import *

class pregunta_Vicky_Form(ModelForm):

    class Meta:
        model = preguntas_Vicky
        fields = ('pregunta', 'respuesta', 'acierto')