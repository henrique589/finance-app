from django import forms
from .models import Lancamento

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