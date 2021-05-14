from django.forms import ModelForm
from .models import Post

class pregunta_Vicky_Form(ModelForm):

    class Meta:
        model = Post
        fields = ('Pregunta')