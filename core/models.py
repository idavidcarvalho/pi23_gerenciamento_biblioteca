from django.db import models

class Usuario(models.Model):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome_completo = models.CharField('Nome Completo', max_length=60, null=True)
    data_nascimento = models.DateField('Data de Nascimento', null=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['username']
