from django.urls import path
from . import views
from financas.views import registro

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
]