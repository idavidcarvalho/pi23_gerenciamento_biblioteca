from django import forms
from .models import Usuario, Cargo, Autor, Editora, Classificacao, Secao, Estado, TipoPeriodico, Produtora
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'rg', 'email','telefone', 'nome_completo', 'data_nascimento', 'password1', 'password2']

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

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['nome']

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome']

class TipoPeriodicoForm(forms.ModelForm):
    class Meta:
        model = TipoPeriodico
        fields = ['nome']

class ProdutoraForm(forms.ModelForm):
    class Meta:
        model = Produtora
        fields = ['nome']

