from django import forms
from .models import Lancamento
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LancamentoForm(forms.ModelForm):
    
    class Meta:
        model = Lancamento
        fields = [
            "data",
            "valor",
            "categoria",
            "tipo",
            "forma_pagamento",
            "parcela_atual",
            "total_parcelas",
        ]

        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nome")
    last_name = forms.CharField(required=True, label="Sobrenome")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']