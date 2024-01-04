from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', autenticar, name= 'login'),
    path('login/', desconectar, name='logout'),
    path('minha/conta/', conta, name='minha_conta'),
    path('acervo/', acervo, name='acervo'),
    path('sobre/', saiba_mais, name='saiba_mais'),

    path('autor/', autor, name='autor'),
    path('autor/cadastro/', cadastro_autor, name='cadastro_autor'),
    path('autor/editar/<int:id>/', editar_autor, name='editar_autor'),
    path('autor/remover/<int:id>/', remover_autor, name='remover_autor'),
     
    path('editora/', editora, name='editora'),
    path('editora/cadastro/', cadastro_editora, name='cadastro_editora'),
    path('editora/editar/<int:id>/', editar_editora, name='editar_editora'),
    path('editora/remover/<int:id>/', remover_editora, name='remover_editora'),

    path('classificacao/', classificacao, name='classificacao'),
    path('classificacao/cadastro/', cadastro_classificacao, name='cadastro_classificacao'),
    path('classificacao/editar/<int:id>/', editar_classificacao, name='editar_classificacao'),
    path('classificacao/remover/<int:id>/', remover_classificacao, name='remover_classificacao'),

    path('secao/', secao, name='secao'),
    path('secao/cadastro/', cadastro_secao, name='cadastro_secao'),
    path('secao/editar/<int:id>/', editar_secao, name='editar_secao'),
    path('secao/remover/<int:id>/', remover_secao, name='remover_secao'),

    path('estado/', estado, name='estado'),
    path('estado/cadastro/', cadastro_estado, name='cadastro_estado'),
    path('estado/editar/<int:id>/', editar_estado, name='editar_estado'),
    path('estado/remover/<int:id>/', remover_estado, name='remover_estado'),
    
    path('tipoperiodico/', tipo_periodico, name='tipo_periodico'),
    path('tipoperiodico/cadastro/', cadastro_tipo_periodico, name='cadastro_tipo_periodico'),
    path('tipoperiodico/editar/<int:id>/', editar_tipo_periodico, name='editar_tipo_periodico'),
    path('tipoperiodico/remover/<int:id>/', remover_tipo_periodico, name='remover_tipo_periodico'),

    path('produtora/', produtora, name='produtora'),
    path('produtora/cadastro/', cadastro_produtora, name='cadastro_produtora'),
    path('produtora/editar/<int:id>/', editar_produtora, name='editar_produtora'),
    path('produtora/remover/<int:id>/', remover_produtora, name='remover_produtora'),

    path('funcionario/', usuario, name='usuario'),
    path('funcionario/cadastro/', cadastro_usuario, name='cadastro_usuario'),
    path('funcionario/editar/<int:id>/', editar_usuario, name='editar_usuario'),
    path('funcionario/remover/<int:id>/', remover_usuario, name='remover_usuario'),
    path('funcionario/desativar/<int:id>/', desativar_usuario, name='desativar_usuario'),

    
    path('livro/', livro, name='livro'),
    path('livro/cadastro/', cadastro_livro, name='cadastro_livro'),
    path('livro/editar/<int:registro>/', editar_livro, name='editar_livro'),
    path('livro/remover/<int:registro>/', remover_livro, name='remover_livro'),
    path('livro/descartar/<int:registro>/', descartar_livro, name='descartar_livro'),


    path('periodico/', periodico, name='periodico'),
    path('periodico/cadastro/', cadastro_periodico, name='cadastro_periodico'),
    path('periodico/editar/<int:registro>/', editar_periodico, name='editar_periodico'),
    path('periodico/remover/<int:registro>/', remover_periodico, name='remover_periodico'),
    path('periodico/descartar/<int:registro>', descartar_periodico, name='descartar_periodico'),

    path('hemeroteca/', hemeroteca, name='hemeroteca'),
    path('hemeroteca/cadastro/', cadastro_hemeroteca, name='cadastro_hemeroteca'),
    path('hemeroteca/editar/<int:registro>/', editar_hemeroteca, name='editar_hemeroteca'),
    path('hemeroteca/remover/<int:registro>', remover_hemeroteca, name='remover_hemeroteca'),
    path('hemeroteca/descartar/<int:registro>', cancelar_hemeroteca, name='cancelar_hemeroteca'),


    path('multimidia/', multimidia, name='multimidia'),
    path('multimidia/cadastro/', cadastro_multimidia, name='cadastro_multimidia'),
    path('multimidia/editar/<int:registro>/', editar_multimidia, name='editar_multimidia'),
    path('multimidia/remover/<int:registro>', remover_multimidia, name='remover_multimidia'),   

    path('leitor/', leitor, name='leitor'),
    path('leitor/cadastro/', cadastro_leitor, name='cadastro_leitor'),
    path('leitor/editar/<int:rg>/', editar_leitor, name='editar_leitor'),
    path('leitor/remover/<int:rg>', remover_leitor, name='remover_leitor'),   

    path('emprestimo/', emprestimo, name='emprestimo'),
    path('emprestimo/cadastro/', cadastro_emprestimo, name='cadastro_emprestimo'),
    #path('emprestimo/remover/<int:id>', remover_emprestimo, name='remover_emprestimo'),   
]
