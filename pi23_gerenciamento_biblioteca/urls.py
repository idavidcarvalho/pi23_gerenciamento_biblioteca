from django.contrib import admin
from django.urls import path
from core.views import autenticar, desconectar
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', perfil, name='perfil'),
    path('', autenticar, name= 'login'),
    path('login/', desconectar, name='logout'),
    path('index/', index),

    path('cargos/', cargo, name='cargos'),
    path('cadastro_cargo/', cadastro_cargo, name='cadastro_cargo'),
    path('editar_cargo/<int:id>/', editar_cargo, name='editar_cargo'),
    path('remover_cargo/<int:id>/', remover_cargo, name='remover_cargo'),

    path('autor/', autor, name='autor'),
    path('cadastro_autor/', cadastro_autor, name='cadastro_autor'),
    path('editar_autor/<int:id>/', editar_autor, name='editar_autor'),
    path('remover_autor/<int:id>/', remover_autor, name='remover_autor'),
     
    path('editora/', editora, name='editora'),
    path('cadastro_editora/', cadastro_editora, name='cadastro_editora'),
    path('editar_editora/<int:id>/', editar_editora, name='editar_editora'),
    path('remover_editora/<int:id>/', remover_editora, name='remover_editora'),

    path('classificacao/', classificacao, name='classificacao'),
    path('cadastro_classificacao/', cadastro_classificacao, name='cadastro_classificacao'),
    path('editar_classificacao/<int:id>/', editar_classificacao, name='editar_classificacao'),
    path('remover_classificacao/<int:id>/', remover_classificacao, name='remover_classificacao'),

    path('secao/', secao, name='secao'),
    path('cadastro_secao/', cadastro_secao, name='cadastro_secao'),
    path('editar_secao/<int:id>/', editar_secao, name='editar_secao'),
    path('remover_secao/<int:id>/', remover_secao, name='remover_secao'),

    path('estado/', estado, name='estado'),
    path('cadastro_estado/', cadastro_estado, name='cadastro_estado'),
    path('editar_estado/<int:id>/', editar_estado, name='editar_estado'),
    path('remover_estado/<int:id>/', remover_estado, name='remover_estado'),
    
    path('tipo_periodico/', tipo_periodico, name='tipo_periodico'),
    path('cadastro_tipo_periodico/', cadastro_tipo_periodico, name='cadastro_tipo_periodico'),
    path('editar_tipo_periodico/<int:id>/', editar_tipo_periodico, name='editar_tipo_periodico'),
    path('remover_tipo_periodico/<int:id>/', remover_tipo_periodico, name='remover_tipo_periodico'),

    path('produtora/', produtora, name='produtora'),
    path('cadastro_produtora/', cadastro_produtora, name='cadastro_produtora'),
    path('editar_produtora/<int:id>/', editar_produtora, name='editar_produtora'),
    path('remover_produtora/<int:id>/', remover_produtora, name='remover_produtora'),

    path('usuario/', usuario, name='usuario'),
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('editar_usuario/<int:id>/', editar_usuario, name='editar_usuario'),
    path('remover_usuario/<int:id>/', remover_usuario, name='remover_usuario'),

    path('livro/', livro, name='livro'),
    path('cadastro_livro/', cadastro_livro, name='cadastro_livro'),
    path('editar_livro/<int:registro>/', editar_livro, name='editar_livro'),
    path('remover_livro/<int:registro>/', remover_livro, name='remover_livro')
]
