from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categorias"
    )

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class FormaPagamento(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="formas_pagamento"
    )

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Lancamento(models.Model):

    TIPO_CHOICES = [
        ("R", "Receita"),
        ("D", "Despesa"),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lancamentos"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    forma_pagamento = models.ForeignKey(
        FormaPagamento,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    data = models.DateTimeField()

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    parcela_atual = models.IntegerField(
        null=True,
        blank=True
    )

    total_parcelas = models.IntegerField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.valor}"
