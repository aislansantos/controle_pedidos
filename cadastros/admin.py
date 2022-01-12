from django.contrib import admin

# Register your models here.
from cadastros.models import Cliente, Fornecedor, Filial, Vendedor, Grupo, Produto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'descricao', 'fornecedor', 'estoque',)
