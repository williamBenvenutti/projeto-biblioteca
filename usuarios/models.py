from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    rua = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    numero = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=11)
    data_lancamento = models.DateField()
    genero = models.CharField(max_length=100)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo