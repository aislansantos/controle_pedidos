from turtle import mode
from django import forms
from .models import Cliente, Fornecedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome']
        
        
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields=['descricao']