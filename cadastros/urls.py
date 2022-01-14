from django.urls import path
from . import views
import cadastros


urlpatterns = [
    path('', views.home, name='home'),

]


# urls clientes
urlpatterns += [
    path('clientes/', views.list_clientes, name='list_clientes'),
    path('cliente/novo', views.new_cliente, name='new_cliente'),
    path('cliente/deletar/<int:pk>/', views.delete_cliente, name="delete_cliente"),
    path('cliente/<int:pk>', views.detail_cliente, name='detail_cliente'),
    path('cliente/<int:pk>/edit', views.edit_cliente, name='edit_cliente'),
]
