from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CargoForm, AutorForm, EditoraForm, ClassificacaoForm
from .models import Cargo, Autor, Editora, Classificacao

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect ('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')

def desconectar(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')


#-------- CRUD Cargo -----

def cadastro_cargo(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cargos')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_cargo.html', contexto)


def cargo(request):
    listar_cargos = Cargo.objects.all()
    contexto = {
        'listar_cargos': listar_cargos
    }
    return render(request, 'cargo.html', contexto)


def editar_cargo(request, id):
    cargo = Cargo.objects.get(pk=id)
    form = CargoForm(request.POST or None, instance=cargo)
    if form.is_valid():
        form.save()
        return redirect('cargos')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_cargo.html', contexto)


def remover_cargo (request,id):
    cargo = Cargo.objects.get(pk=id)
    cargo.delete()
    return redirect('cargos')


# ------- CRUD Autor -------
def cadastro_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('autor')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_autor.html', contexto)


def autor(request):
    listar_autor = Autor.objects.all()
    contexto = {
        'listar_autor': listar_autor
    }
    return render(request, 'autor.html', contexto)


def editar_autor(request, id):
    autor = Autor.objects.get(pk=id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('autor')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_autor.html', contexto)


def remover_autor (request,id):
    autor = Autor.objects.get(pk=id)
    autor.delete()
    return redirect('autor')

# -------- CRUD Editora -----------
def cadastro_editora(request):
    form = EditoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('editora')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_editora.html', contexto)


def editora(request):
    listar_editora = Editora.objects.all()
    contexto = {
        'listar_editora': listar_editora
    }
    return render(request, 'editora.html', contexto)


def editar_editora(request, id):
    editora = Editora.objects.get(pk=id)
    form = EditoraForm(request.POST or None, instance=editora)
    if form.is_valid():
        form.save()
        return redirect('editora')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_editora.html', contexto)


def remover_editora (request,id):
    editora = Editora.objects.get(pk=id)
    editora.delete()
    return redirect('editora')

# ------ CRUD Classificação -----------

def cadastro_classificacao(request):
    form = ClassificacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('classificacao')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_classificacao.html', contexto)


def classificacao(request):
    listar_classificacao = Classificacao.objects.all()
    contexto = {
        'listar_classificacao': listar_classificacao
    }
    return render(request, 'classificacao.html', contexto)


def editar_classificacao(request, id):
    classificacao = Classificacao.objects.get(pk=id)
    form = ClassificacaoForm(request.POST or None, instance=classificacao)
    if form.is_valid():
        form.save()
        return redirect('classificacao')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_classificacao.html', contexto)


def remover_classificacao (request,id):
    classificacao = Classificacao.objects.get(pk=id)
    classificacao.delete()
    return redirect('classificacao')