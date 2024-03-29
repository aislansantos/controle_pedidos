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
    path('cliente/<int:pk>/edit', views.edit_cliente, name='edit_cliente'),
]


# urls Fornecedores
urlpatterns += [
    path('fornecedores/', views.list_fornecedores, name='list_fornecedores'),
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
    path('vendedor/<int:pk>/deletar', views.delete_vendedor, name='delete_vendedor')
]

#urls Grupos
urlpatterns += [
    path('grupos/', views.list_grupos, name='list_grupos'),
    path('grupo/novo', views.new_grupo, name='new_grupo'),
    path('grupo/<int:pk>/edit', views.edit_grupo, name='edit_grupo'),
    path('grupo/<int:pk>/deletar', views.delete_grupo, name='delete_grupo')
]


#urls Grupos
urlpatterns +=[
    path('produtos/', views.list_produtos, name='list_produtos'),
    path('produto/novo', views.new_produto, name='new_produto'),
    path('produto/<int:pk>/edit', views.edit_produto, name='edit_produto'),
    path('produto/<int:pk>/delete', views.delete_produto, name='delete_produto'),
]