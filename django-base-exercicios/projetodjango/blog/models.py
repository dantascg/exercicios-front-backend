from django.db import models
from django.conf import settings

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pessoa(models.Model):

    # CharField - usado para strings curtas, precisa de max_length
    nome = models.CharField(max_length=100)

    # TextField - usado para textos longos
    biografia = models.TextField(blank=True, null=True)

    # IntegerField - números inteiros
    idade = models.IntegerField()

    # DateField - apenas data (sem hora)
    data_nascimento = models.DateField()

    # DateTimeField - data e hora
    criado_em = models.DateTimeField(auto_now_add=True)   # preenchido automaticamente na criação
    atualizado_em = models.DateTimeField(auto_now=True)   # atualizado sempre que salvar

    # EmailField - valida formato de e-mail automaticamente
    email = models.EmailField(unique=True)

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True
    )

    def __str__(self):
        return f"{self.nome} ({self.email})"
    