import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Fornecedor
from .forms import ClienteForm, FornecedorForm

# Create your views here.

# redicionamento de paginas

'''
    Cadastro de Clientes
'''


def home(request):
    return render(request, 'cadastros/index.html')


def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/clientes.html', {'clientes': clientes})


def detail_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cadastros/clientes_cadastro.html', {'cliente': cliente})


def new_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            clientes = Cliente.objects.all()
            return render(request, 'cadastros/clientes.html', {'clientes': clientes})
    else:
        form = ClienteForm()
        return render(request, 'cadastros/clientes_cadastro.html', {'form': form})
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/clientes.html', {'clientes': clientes})


def edit_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)  # o que é
        if form.is_valid():
            form.save()
            return redirect('list_clientes')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'cadastros/clientes_cadastro.html', {'form': form})
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/clientes.html', {'clientes': clientes})


def delete_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('list_clientes')


'''
    Cadastro de Fornecedores
'''


def list_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores.html', {'fornecedores': fornecedores})


def detail_fornecedor(request):
    fornecedor = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores_cadastro.html', {'fornecedor': fornecedor})


def new_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            fornecedores = Fornecedor.objects.all()
            return redirect('list_fornecedores')
    else:
        form = FornecedorForm()
        return render(request, 'cadastros/fornecedores_cadastro.html', {'form': form})
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores.html', {'fornecedores': fornecedores})


def edit_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('list_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
        return render(request, 'cadastros/fornecedores_cadastro.html', {'form':form})
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores.html', {'fornecedores': fornecedores})