from django.shortcuts import render, redirect, get_object_or_404
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

def livro_new(request, template_name ='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, template_name, {'form':form})


def livro_edit (request, pk, template_name='livro_form.html'):
    Livro = get_object_or_404(livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance = Livro)
        if form.is_valid():
            Livro = form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance = Livro)

    return render(request, template_name, {'form': form})


def livro_remove(request, pk):
    Livro = livro.objects.get(pk=pk)

    if request.method == "POST":

        Livro.delete()

        return redirect('listar_livros')

    return render(request, 'livro_delete.html', {'Livro': Livro})



# Create your views here.
