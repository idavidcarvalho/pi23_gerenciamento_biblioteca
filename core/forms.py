from django import forms
from .models import Usuario
from core import models

class UsuarioForm(models.Model):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'email', 'nome_completo', 'data_nascimento', 'password1', 'password2']
