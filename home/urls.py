from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name="index" ),
    path('excluir/<int:id>', delete_one, name="excluir" ),
    path('gerenciar/<int:id>/', handle_form, name='atualizar'),
    path('gerenciar/', handle_form, name='gerenciar'),
    path('search/', search, name='search'),
    path('preencher/', gerarDadosFicticios, name='preencher'),


]
