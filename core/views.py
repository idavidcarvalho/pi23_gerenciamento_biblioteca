from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CargoForm, AutorForm, EditoraForm, ClassificacaoForm, SecaoForm, EstadoForm, TipoPeriodicoForm, ProdutoraForm, UsuarioForm
from .models import Cargo, Autor, Editora, Classificacao, Secao, Estado, TipoPeriodico, Produtora, Usuario

@login_required
def perfil(request):
    return render(request, 'perfil.html')

#-------- Login -----
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

#--------- CRUD Seção ------------

def cadastro_secao(request):
    form = SecaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('secao')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_secao.html', contexto)

def secao(request):
    listar_secao = Secao.objects.all()
    contexto = {
        'listar_secao': listar_secao
    }
    return render(request, 'secao.html', contexto)

def editar_secao(request, id):
    secao = Secao.objects.get(pk=id)
    form = SecaoForm(request.POST or None, instance=secao)
    if form.is_valid():
        form.save()
        return redirect('secao')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_secao.html', contexto)

def remover_secao (request,id):
    secao = Secao.objects.get(pk=id)
    secao.delete()
    return redirect('secao')

# ----------- CRUD Estado ------------

def cadastro_estado(request):
    form = EstadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estado')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_estado.html', contexto)

def estado(request):
    listar_estado = Estado.objects.all()
    contexto = {
        'listar_estado': listar_estado
    }
    return render(request, 'estado.html', contexto)

def editar_estado(request, id):
    estado = Estado.objects.get(pk=id)
    form = EstadoForm(request.POST or None, instance=estado)
    if form.is_valid():
        form.save()
        return redirect('estado')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_estado.html', contexto)

def remover_estado (request,id):
    estado = Estado.objects.get(pk=id)
    estado.delete()
    return redirect('estado')

# -------------- CRUD Tipo de Periódico ----------

def cadastro_tipo_periodico(request):
    form = TipoPeriodicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tipo_periodico')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_tipo_periodico.html', contexto)

def tipo_periodico(request):
    listar_tipo_periodico = TipoPeriodico.objects.all()
    contexto = {
        'listar_tipo_periodico': listar_tipo_periodico
    }
    return render(request, 'tipo_periodico.html', contexto)

def editar_tipo_periodico(request, id):
    tipo_periodico = TipoPeriodico.objects.get(pk=id)
    form = TipoPeriodicoForm(request.POST or None, instance=tipo_periodico)
    if form.is_valid():
        form.save()
        return redirect('tipo_periodico')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_tipo_periodico.html', contexto)

def remover_tipo_periodico (request,id):
    tipo_periodico = TipoPeriodico.objects.get(pk=id)
    tipo_periodico.delete()
    return redirect('tipo_periodico')

#------------ CRUD Produtora ----------

def cadastro_produtora(request):
    form = ProdutoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produtora')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_produtora.html', contexto)

def produtora(request):
    listar_produtora = Produtora.objects.all()
    contexto = {
        'listar_produtora': listar_produtora
    }
    return render(request, 'produtora.html', contexto)

def editar_produtora(request, id):
    produtora = Produtora.objects.get(pk=id)
    form = ProdutoraForm(request.POST or None, instance=produtora)
    if form.is_valid():
        form.save()
        return redirect('produtora')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_produtora.html', contexto)

def remover_produtora (request,id):
    produtora = Produtora.objects.get(pk=id)
    produtora.delete()
    return redirect('produtora')

#---------- CRUD Usuário -----------

def cadastro_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuario')
    contexto = {
        'form': form
    }
    return render(request, 'registration/cadastro_usuario.html', contexto)

def usuario(request):
    listar_usuario = Usuario.objects.all()
    contexto = {
        'listar_usuario': listar_usuario
    }
    return render(request, 'usuario.html', contexto)

def editar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('usuario')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_usuario.html', contexto)

def remover_usuario (request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('usuario')