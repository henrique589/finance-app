from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_lancamentos, name='inicio'),
    path('lista_lancamentos/', views.lista_lancamentos, name='lista_lancamentos'),
    path('novo/', views.criar_lancamento, name='criar_lancamento'),
    path('editar/<int:id>/', views.editar_lancamento, name='editar_lancamento'),
    path('deletar/<int:id>/', views.deletar_lancamento, name='deletar_lancamento'),
]