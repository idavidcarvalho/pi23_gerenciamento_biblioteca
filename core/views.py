from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import  AutorForm, EditoraForm, ClassificacaoForm, SecaoForm, EstadoForm, TipoPeriodicoForm, LivroForm, ProdutoraForm, UsuarioForm, PeriodicoForm
from .models import Autor, Editora, Classificacao, Secao, Estado, TipoPeriodico, Produtora, Usuario, Livro, Periodico
from django.contrib.auth.models import Permission

def permissaoCoodenadorBibliotecario(Usuario):
    return user_passes_test('core.coordenador') or user_passes_test('core.bibliotecario')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def conta(request):
    return render(request, 'minha_conta.html')

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

# -------- CRUD Editora -----------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_editora(request):
    form = EditoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('editora')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_editora.html', contexto)

@login_required
def editora(request):
    listar_editora = Editora.objects.all()
    contexto = {
        'listar_editora': listar_editora
    }
    return render(request, 'editora.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_editora (request,id):
    editora = Editora.objects.get(pk=id)
    editora.delete()
    return redirect('editora')

# ------ CRUD Classificação -----------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_classificacao(request):
    form = ClassificacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('classificacao')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_classificacao.html', contexto)

@login_required
def classificacao(request):
    listar_classificacao = Classificacao.objects.all()
    contexto = {
        'listar_classificacao': listar_classificacao
    }
    return render(request, 'classificacao.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_classificacao (request,id):
    classificacao = Classificacao.objects.get(pk=id)
    classificacao.delete()
    return redirect('classificacao')

#--------- CRUD Seção ------------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_secao(request):
    form = SecaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('secao')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_secao.html', contexto)

@login_required
def secao(request):
    listar_secao = Secao.objects.all()
    contexto = {
        'listar_secao': listar_secao
    }
    return render(request, 'secao.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_tipo_periodico(request):
    form = TipoPeriodicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tipo_periodico')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_tipo_periodico.html', contexto)

@login_required
def tipo_periodico(request):
    listar_tipo_periodico = TipoPeriodico.objects.all()
    contexto = {
        'listar_tipo_periodico': listar_tipo_periodico
    }
    return render(request, 'tipo_periodico.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_tipo_periodico (request,id):
    tipo_periodico = TipoPeriodico.objects.get(pk=id)
    tipo_periodico.delete()
    return redirect('tipo_periodico')

#------------ CRUD Produtora ----------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_produtora(request):
    form = ProdutoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produtora')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_produtora.html', contexto)

@login_required
def produtora(request):
    listar_produtora = Produtora.objects.all()
    contexto = {
        'listar_produtora': listar_produtora
    }
    return render(request, 'produtora.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_produtora (request,id):
    produtora = Produtora.objects.get(pk=id)
    produtora.delete()
    return redirect('produtora')

# ------- CRUD Autor -------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('autor')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_autor.html', contexto)

@login_required
def autor(request):
    listar_autor = Autor.objects.all()
    contexto = {
        'listar_autor': listar_autor
    }
    return render(request, 'autor.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_autor (request,id):
    autor = Autor.objects.get(pk=id)
    autor.delete()
    return redirect('autor')

#---------- CRUD Usuário -----------
@login_required
@permission_required('core.coordenador')
def cadastro_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
       usuario = form.save(commit=False)
       usuario.save()
    
       #Alterando permissão

       # Recupera a permissão selecionada
       permissao_selecionada = request.POST['permissao']

       # Recupara a permissão selcioanda no BD
       permissao = Permission.objects.get(codename = permissao_selecionada)
        
       # Adcionar permissão ao usuario que está sendo cadastrado
       usuario.user_permissions.add(permissao)
       usuario.save()
       return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registration/cadastro_usuario.html', contexto)

@login_required
@permission_required('core.coordenador')
def usuario(request):
    listar_usuario = Usuario.objects.all()
    contexto = {
        'listar_usuario': listar_usuario
    }
    return render(request, 'usuario.html', contexto)

@login_required
@permission_required('core.coordenador')
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

@login_required
@permission_required('core.coordenador')
def remover_usuario (request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('usuario')

# -------------- CRUD Livro ----------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livro')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_livro.html', contexto)

@login_required
def livro(request):
    listar_livro = Livro.objects.all()
    contexto = {
        'listar_livro': listar_livro
    }
    return render(request, 'livro.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def editar_livro(request, registro):
    livro = Livro.objects.get(pk=registro)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('livro')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_livro.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_livro (request,registro):
    livro = Livro.objects.get(pk=registro)
    livro.delete()
    return redirect('livro')

#----------- CRUD Periódico ------------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_periodico(request):
    form = PeriodicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('periodico')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_periodico.html', contexto)

@login_required
def periodico(request):
    listar_periodico = Periodico.objects.all()
    contexto = {
        'listar_periodico': listar_periodico
    }
    return render(request, 'periodico.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def editar_periodico(request, registro):
    periodico = Periodico.objects.get(pk=registro)
    form = PeriodicoForm(request.POST or None, instance=periodico)
    if form.is_valid():
        form.save()
        return redirect('periodico')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_periodico.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_periodico (request, registro):
    periodico = Periodico.objects.get(pk=registro)
    periodico.delete()
    return redirect('periodico')
