from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import  AutorForm, EditoraForm, ClassificacaoForm, SecaoForm, EstadoForm, TipoPeriodicoForm, LivroForm, ProdutoraForm, UsuarioForm, PeriodicoForm, HemerotecaForm, MultimidiaForm, LeitorForm, EmprestimoForm
from .models import Autor, Editora, Classificacao, Secao, Estado, TipoPeriodico, Produtora, Usuario, Livro, Periodico, Emprestimo, Hemeroteca, Leitor, Multimidia, Emprestimo
from django.contrib.auth.models import Permission
from django.db import IntegrityError
from django.utils import timezone
from django_q.models import Schedule


def permissaoCoodenadorBibliotecario(Usuario):
    return user_passes_test('core.coordenador') or user_passes_test('core.bibliotecario')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def conta(request):
    return render(request, 'minha_conta.html')

@login_required
def acervo(request):
    return render(request, 'acervo.html')

def saiba_mais(request):
    return render(request, 'saiba_mais.html')

#-------- Login -----
def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect ('home')
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
    nome = ''
    if request.POST:
        nome = request.POST['nome']
        listar_editora = Editora.objects.filter(nome__contains=nome)
    else:
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
    nome = ''
    if request.POST:
        nome = request.POST['nome']
        listar_classificacao = Classificacao.objects.filter(nome__contains=nome)
    else:
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
    nome = ''
    if request.POST:
        nome = request.POST['nome']
        listar_secao = Secao.objects.filter(nome__contains=nome)
    else:
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
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
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
    nome = ''
    if request.POST:
        nome = request.POST['nome']
        listar_tipo_periodico = TipoPeriodico.objects.filter(nome__contains=nome)
    else:
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
    nome = ''
    if request.POST:
        nome = request.POST['nome']
        listar_produtora = Produtora.objects.filter(nome__contains=nome)
    else: 
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
    nome = ''
    if request.POST:
        nome = request.POST['nome']
        listar_autor = Autor.objects.filter(nome__contains=nome)
    else:
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
    cpf = ''
    if request.POST:
        cpf = request.POST['cpf']
        listar_usuario = Usuario.objects.filter(cpf__contains=cpf)
    else:
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

@login_required
@permission_required('core.coordenador')
def desativar_usuario(request, id):
   usuario = Usuario.objects.get(pk=id)
   usuario.status = 'Inativo'
   usuario.save()
   return redirect('usuario')

# -------------- CRUD Livro ----------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        livro = form.save(commit=False)
        livro.criado_por = request.user
        livro.save()
        return redirect('livro')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_livro.html', contexto)

@login_required
def livro(request):
    titulo = ''
    status =''
    autor = ''
    if request.POST:
        autor = request.POST['autor']
        titulo = request.POST['titulo']
        status = request.POST['status']
        if request.POST['status'] =='1':
            listar_livro = Livro.objects.filter(titulo__contains=titulo).filter(status='Descartado')
        elif request.POST['status'] == '2':
            listar_livro = Livro.objects.filter(titulo__contains=titulo).filter(status='ativo')
        elif request.POST['status'] == '-1':
            listar_livro = Livro.objects.all()
        elif request.POST['status'] == '3':
            listar_livro = Livro.objects.filter(titulo__contains=titulo).filter(status='emprestado')
        elif request.POST['status'] == '4':
            listar_livro = Livro.objects.filter(titulo__contains=titulo).filter(status='extraviado')

    else:
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def descartar_livro(request, registro):
    livro = Livro.objects.get(pk=registro)
    livro.status = 'Descartado'
    livro.save()
    return redirect('livro')

#----------- CRUD Periódico ------------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_periodico(request):
    form = PeriodicoForm(request.POST or None)
    
    if form.is_valid():
        periodico = form.save(commit=False)
        periodico.criado_por = request.user
        periodico.save()
        return redirect('periodico')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_periodico.html', contexto)

@login_required
def periodico(request):
    titulo = ''
    status =''
    if request.POST:
        titulo = request.POST['titulo']
        status = request.POST['status']
        if request.POST['status'] =='1':
            listar_periodico = Periodico.objects.filter(titulo__contains=titulo).filter(status='Descartado')
        elif request.POST['status'] == '2':
            listar_periodico = Periodico.objects.filter(titulo__contains=titulo).filter(status='ativo')
        elif request.POST['status'] == '-1':
            listar_periodico = Periodico.objects.all()
        elif request.POST['status'] == '3':
            listar_periodico = Periodico.objects.filter(titulo__contains=titulo).filter(status='emprestado')
        elif request.POST['status'] == '4':
            listar_periodico = Periodico.objects.filter(titulo__contains=titulo).filter(status='extraviado')

    else:
        listar_periodico = Periodico.objects.all()
    
    contexto = {
        'listar_periodico': listar_periodico,
        'titulo': titulo,   
    }
    return render(request, 'periodico.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def editar_periodico(request, registro):
    periodico = Periodico.objects.get(pk=registro)
    form = PeriodicoForm(request.POST or None, instance=periodico)
    if form.is_valid():
        form.save()
        #messages.success(request,  'modificado com sucesso!!')
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

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def descartar_periodico(request, registro):
    periodico = Periodico.objects.get(pk=registro)
    periodico.status = 'Descartado'
    periodico.save()
    return redirect('periodico')

# -------- CRUD Hemeroteca -------------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_hemeroteca(request):
    form = HemerotecaForm(request.POST or None)
    if form.is_valid():
        hemeroteca = form.save(commit=False)
        hemeroteca.criado_por = request.user
        hemeroteca.save()
        return redirect('hemeroteca')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_hemeroteca.html', contexto)

@login_required
def hemeroteca(request):
    registro = ''
    if request.POST:
        registro = request.POST['registro']
        listar_hemeroteca = Hemeroteca.objects.filter(registro__contains=registro)
    else: 
        listar_hemeroteca = Hemeroteca.objects.all()
    contexto = {
        'listar_hemeroteca': listar_hemeroteca
    }
    return render(request, 'hemeroteca.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def editar_hemeroteca(request, registro):
    hemeroteca = Hemeroteca.objects.get(pk=registro)
    form = HemerotecaForm(request.POST or None, instance=hemeroteca)
    if form.is_valid():
        form.save()
        return redirect('hemeroteca')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_hemeroteca.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_hemeroteca (request, registro):
    hemeroteca = Hemeroteca.objects.get(pk=registro)
    hemeroteca.delete()
    return redirect('hemeroteca')

def cancelar_hemeroteca(request, registro):
    hemeroteca = Hemeroteca.objects.get(pk=registro)
    hemeroteca.status = 'Descartada'
    hemeroteca.save()
    return redirect('hemeroteca')

# CRUD Multimídia
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_multimidia(request):
    form = MultimidiaForm(request.POST or None)
    if form.is_valid():
        multimidia = form.save(commit=False)
        multimidia.criado_por = request.user
        multimidia.save()
        return redirect('multimidia')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_multimidia.html', contexto)

@login_required
def multimidia(request):
    titulo = ''
    if request.POST:
        titulo = request.POST['titulo']
        listar_multimidia = Multimidia.objects.filter(titulo__contains=titulo)
    else:
        listar_multimidia = Multimidia.objects.all()
    contexto = {
        'listar_multimidia': listar_multimidia
    }
    return render(request, 'multimidia.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def editar_multimidia(request, registro):
    multimidia = Multimidia.objects.get(pk=registro)
    form = MultimidiaForm(request.POST or None, instance=multimidia)
    if form.is_valid():
        form.save()
        return redirect('multimidia')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro_multimidia.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_multimidia (request, registro):
    multimidia = Multimidia.objects.get(pk=registro)
    multimidia.delete()
    return redirect('multimidia')

# ---------- CRUD Leitor --------------
@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def cadastro_leitor(request):
    if request.method == 'POST':
        form = LeitorForm(request.POST, request.FILES)
        if form.is_valid():
            leitor = form.save(commit=False)
            leitor.criado_por = request.user
            leitor.save()
            return redirect('leitor')
    else:
        form = LeitorForm()

    contexto = {
        'form': form
    }
    return render(request, 'cadastro_leitor.html', contexto)

@login_required
def leitor(request):
    rg = ''
    if request.POST:
        rg = request.POST['rg']
        listar_leitor = Leitor.objects.filter(rg__contains=rg)
    else:
        listar_leitor = Leitor.objects.all()
    contexto = {
        'listar_leitor': listar_leitor
    }
    return render(request, 'leitor.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def editar_leitor(request, rg):
    leitor = Leitor.objects.get(pk=rg)

    if request.method == 'POST':
        form = LeitorForm(request.POST, request.FILES, instance=leitor)
        if form.is_valid():
            form.save()
            return redirect('leitor')
    else:
        form = LeitorForm(instance=leitor)

    contexto = {
        'form': form
    }
    return render(request, 'cadastro_leitor.html', contexto)

@login_required
@user_passes_test(permissaoCoodenadorBibliotecario)
def remover_leitor (request, rg):
    leitor = Leitor.objects.get(pk=rg)
    leitor.delete()
    return redirect('leitor')

# ---------- CRUD Empréstimo -----------

@login_required
def cadastro_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        try:
            if form.is_valid():
                emprestimo = form.save(commit=False)
                emprestimo.realizado_por = request.user
                emprestimo.data_emprestimo = timezone.now()
                emprestimo.save()
                
                # Agendar verificação de atraso
                emprestimo_id = emprestimo.id
                Schedule.objects.create(func='core.tasks.verificar_atraso', args=f'{emprestimo_id}', schedule_type=Schedule.ONCE)

                return redirect('emprestimo')
        except IntegrityError:
            form.add_error('livro', "Você deve emprestar um livro ou um periódico.")

    else:
        form = EmprestimoForm()

    contexto = {'form': form}
    return render(request, 'cadastro_emprestimo.html', contexto)

@login_required
def emprestimo(request):
    leitor = ''
    if request.POST:
        leitor = request.POST['leitor']
        listar_emprestimo = Emprestimo.objects.filter(leitor__contains=leitor)
    else:
        listar_emprestimo = Emprestimo.objects.all()
    contexto = {
        'listar_emprestimo': listar_emprestimo
    }
    return render(request, 'emprestimo.html', contexto)
@login_required
def cancelar_emprestimo(request, id):
    emprestimo = Emprestimo.objects.get(pk=id)
    emprestimo.status = 'Cancelado'
    emprestimo.save()
    return redirect('emprestimo')


