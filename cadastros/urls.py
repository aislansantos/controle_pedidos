from django.urls import path
from . import views

# Index
urlpatterns = [
    path('', views.home, name='home'),

]


# urls Clientes
urlpatterns += [
    path('clientes/', views.list_clientes, name='list_clientes'),
    path('cliente/novo', views.new_cliente, name='new_cliente'),
    path('cliente/deletar/<int:pk>/', views.delete_cliente, name="delete_cliente"),
    path('cliente/<int:pk>', views.detail_cliente, name='detail_cliente'),
    path('cliente/<int:pk>/edit', views.edit_cliente, name='edit_cliente'),
]


# urls Fornecedores
urlpatterns += [
    path('fornecedores/', views.list_fornecedores, name='list_fornecedores'),
    path('fornecedor/<int:pk>', views.detail_fornecedor, name="detail_fornecedor"),
    path('fornecedor/novo', views.new_fornecedor, name='new_fornecedor'),
    path('fornedor/<int:pk>/edit', views.edit_fornecedor, name='edit_fornecedor',),
    path('fornecedor/deletar/<int:pk>', views.delete_fornecedor, name='delete_fornecedor'),
]


# urls Filiais
urlpatterns += [
    path('filiais/', views.list_filiais, name='list_filiais'),
    path('filial/novo', views.new_filial, name='new_filial'),
    path('filial/<int:pk>/edit', views.edit_filial, name='edit_filial'),
    path('filial/<int:pk>/deletar', views.delete_filial, name='delete_filial')
]

#urls Vendedores
urlpatterns += [
    path('vendedores/', views.list_vendedores, name='list_vendedores'),
    path('vendedor/novo', views.new_vendedor, name='new_vendedor'),
    path('vendedor/<int:pk>/edit', views.edit_vendedor, name='edit_vendedor'),
]