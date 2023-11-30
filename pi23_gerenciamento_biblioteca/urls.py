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
    
]
