from django.db import models, IntegrityError, transaction
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_q.models import Schedule


class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField('RG', max_length=14, unique=True)
    nome_completo = models.CharField('Nome Completo', max_length=60, null=False)
    data_nascimento = models.DateField('Data de Nascimento', null=True)
    email = models.CharField('Email:', max_length=100, null=False)
    telefone = models.CharField('Telefone:', max_length=11, null= False)
    foto = models.ImageField(upload_to='funcionarios', null=False)
    status = models.CharField(max_length=45,choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo')
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['username']

    class Meta:
        permissions = [
            ('coordenador','Poderá gerenciar acervo, empréstimos, leitores e funcionários'),
            ('bibliotecario','Poderá gerenciar acervo, empréstimos e leitores'),
            ('auxiliar','Poderá gerenciar empréstimos e leitores'),

        ]
    def __str__(self):
        return self.nome_completo

    

# Define the `Autor` model
class Autor(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

# Define the `Editora` model
class Editora(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

# Define the `Classificacao` model
class Classificacao(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

# Define the `Secao` model
class Secao(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

# Define the `Estado` model
class Estado(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

# Define the `Livro` model
class Livro(models.Model):
    registro = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=45)
    paginas = models.IntegerField()
    edicao = models.IntegerField()
    dataLancamento = models.DateField()
    status = models.CharField(max_length=45,choices=[('ativo', 'Ativo'), ('emprestado', 'Emprestado'), ('extraviado','Extraviado'),('descartado','Descartato')], default='ativo')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

# Define the `TipoPeriodico` model
class TipoPeriodico(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

# Define the `Periodico` model
class Periodico(models.Model):
    registro = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=200)
    numero = models.IntegerField()
    tipoPeriodico = models.ForeignKey(TipoPeriodico, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    status = models.CharField(max_length=45,choices=[('ativo', 'Ativo'), ('emprestado', 'Emprestado'), ('extraviado','Extraviado'),('descartado','Descartado')], default='ativo')
    criado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

# Define the `Produtora` model
class Produtora(models.Model):
    nome = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nome

# Define the `Multimidia` model
class Multimidia(models.Model):
    registro = models.IntegerField(primary_key=True)
    data = models.DateField()
    titulo = models.CharField(max_length=45)
    subtitulo = models.CharField(max_length=45, null=True)
    produtora = models.ForeignKey(Produtora, on_delete=models.CASCADE)
    status = models.CharField(max_length=45,choices=[('ativo', 'Ativo'),('descartado','Descartato')], default='ativo')
    criado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

# Define the `Leitor` model
class Leitor(models.Model):
    rg = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    profissao = models.CharField(max_length=45)
    instituicao = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    foto = models.ImageField(upload_to='leitores', null=False)
    criado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

# Define the `Emprestimo` model
from django.db import models, IntegrityError

from django.db import models
from django.utils import timezone
from django_q.models import Schedule

from django.db import models

class Emprestimo(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    periodico = models.ForeignKey(Periodico, on_delete=models.CASCADE, null=True, default=None)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, default=None)
    status = models.CharField(max_length=45, choices=[('em andamento', 'Em andamento'), ('cancelado', 'Cancelado'), ('devolvido', 'Devolvido'), ('atrasado', 'Atrasado')], default='em andamento')
    realizado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    justificativa = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Emprestimo {self.id}"

    def save(self, *args, **kwargs):
        if not self.id:  # Verifica se é um novo empréstimo (não uma atualização)
            # Atualiza o status do livro se houver um livro associado ao empréstimo
            if self.livro:
                self.livro.status = 'emprestado'
                self.livro.save()

            # Atualiza o status do periódico se houver um periódico associado ao empréstimo
            if self.periodico:
                self.periodico.status = 'emprestado'
                self.periodico.save()

        super().save(*args, **kwargs)


# Define the `Hemeroteca` model
class Hemeroteca(models.Model):
    registro = models.IntegerField(primary_key=True)
    assunto = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=100, null=True)
    obs = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=45,choices=[('ativo', 'Ativo'),('descartado','Descartato')], default='ativo')
    criado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.assunto