from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topico(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome


class Sala(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topico = models.ForeignKey(Topico, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    atualizacao = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-atualizacao', '-criado']

    def __str__(self) -> str:
        return self.nome
    
class Mensagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    assunto = models.TextField()
    atualizacao = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.assunto
