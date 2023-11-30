from django import forms
from .models import Usuario, Cargo, Autor, Editora, Classificacao
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'email', 'nome_completo', 'data_nascimento', 'password1', 'password2']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nome']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class ClassificacaoForm(forms.ModelForm):
    class Meta:
        model = Classificacao
        fields = ['nome']