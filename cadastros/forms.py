from turtle import mode
from django import forms
from .models import Cliente, Fornecedor, Filial, Vendedor, Grupo, Produto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome']
        
        
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields=['descricao']
        
class FilialForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = ['descricao']
        
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome']


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['descricao']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'descricao',
            'grupo',
            'fornecedor',
            'estoque'
                  ]