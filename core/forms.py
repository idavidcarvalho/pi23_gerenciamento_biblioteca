from django import forms
from .models import Usuario, Autor, Editora, Classificacao, Secao, Estado, TipoPeriodico, Produtora, Livro, Periodico, Emprestimo, Hemeroteca, Leitor, Multimidia
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'rg', 'email','telefone', 'nome_completo', 'data_nascimento', 'password1',]

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

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'registro', 'paginas', 'edicao', 'dataLancamento', 'autor', 'editora', 'classificacao', 'secao', 'estado']

class PeriodicoForm(forms.ModelForm):
    class Meta:
        model = Periodico
        fields = ['registro', 'titulo', 'numero', 'tipoPeriodico', 'autor', 'editora', 'secao']

class HemerotecaForm(forms.ModelForm):
    class Meta:
        model = Hemeroteca
        fields = ['registro', 'assunto', 'fornecedor', 'obs']

class MultimidiaForm(forms.ModelForm):
    class Meta:
        model = Multimidia
        fields = ['registro','data', 'titulo', 'subtitulo', 'produtora']

class LeitorForm(forms.ModelForm):
    class Meta: 
        model = Leitor
        fields = ['rg', 'nome','profissao', 'instituicao', 'telefone', 'email', 'endereco', 'foto']

class EmprestimoForm(forms.ModelForm):
    livro = forms.ModelChoiceField(queryset=Livro.objects.all(), required=False)
    periodico = forms.ModelChoiceField(queryset=Periodico.objects.all(), required=False)
    class Meta: 
        model = Emprestimo
        fields = ['justificativa', 'leitor', 'periodico', 'livro']