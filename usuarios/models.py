from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=35)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=80)

class Pessoa(models.Model):
    nome = models.CharField(max_length=35)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()
    rua = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    numero = models.IntegerField()