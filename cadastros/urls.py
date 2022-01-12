from django.urls import path
from . import views
import cadastros

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.list_clientes, name='list_clientes'),
    path('clientes_cadastro/', views.clientes_cadastro, name='clientes_cadastro')
    
]