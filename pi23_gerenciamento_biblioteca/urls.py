from django.contrib import admin
from django.urls import path
from core.views import autenticar, desconectar
from core.views import perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', perfil, name='perfil'),
    path('', autenticar, name= 'login'),
    path('login/', desconectar, name='logout'),
]
