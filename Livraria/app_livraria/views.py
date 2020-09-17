from django.shortcuts import render
from .models import *
from django.forms import ModelForm

class LivroForm(ModelForm):
    class Meta:
        model = livro
        fields = ['Autor', 'Editora', 'Paginas', 'Titulo', 'ano', 'Email']


def livro_list(request, template_name='livro_list.html'):
    Livro = livro.objects.all()
    Livros = {'lista': Livro}
    return render(request, template_name, Livros)

# Create your views here.
