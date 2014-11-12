from django.db import models

class Produto (models.Model):
    produto = models.CharField(max_length=70)
    fornecedor = models.CharField(max_length=100)
    email = models.EmailField(),
    telefone = models.CharField(max_length=25)
    