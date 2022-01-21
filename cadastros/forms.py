from turtle import mode
from django import forms
from .models import Cliente, Fornecedor, Filial, Vendedor

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
        