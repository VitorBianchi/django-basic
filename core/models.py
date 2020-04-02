from django.db import models

# Create your models here.
class Product(models.Model):
    nome  = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome


class Client(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.nome