from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Lancamento
from .forms import LancamentoForm

@login_required
def home(request):
    return render(request, 'financas/home.html')

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "financas/registro.html", {"form": form})

@login_required
def criar_lancamento(request):
    if request.method == "POST":
        form = LancamentoForm(request.POST)

        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.usuario = request.user
            lancamento.save()

            return redirect("lista_lancamentos")
    
    else:
        form = LancamentoForm()
    
    return render(request, "financas/criar_lancamento.html", {"form": form})

@login_required
def lista_lancamentos(request):
    lancamentos = Lancamento.objects.filter(
        usuario = request.user
    ).order_by("-data")

    return render(request, "financas/lista_lancamentos.html", {"lancamentos": lancamentos})

@login_required
def editar_lancamento(request, id):
    lancamento = get_object_or_404(
        Lancamento, 
        id=id, 
        usuario=request.user
    )

    if request.method == "POST":
        form = LancamentoForm(request.POST, instance=lancamento)

        if form.is_valid():
            form.save()
            return redirect("lista_lancamentos")
    else:
        form = LancamentoForm(instance=lancamento)
    
    return render(request, "financas/criar_lancamento.html", {"form": form})

@login_required
def deletar_lancamento(request, id):
    lancamento = get_object_or_404(
        Lancamento,
        id=id,
        usuario = request.user
    )

    lancamento.delete()

    return render("lista_lancamentos")