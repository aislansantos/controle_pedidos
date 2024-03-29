import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Fornecedor, Filial, Vendedor, Grupo, Produto
from .forms import ClienteForm, FornecedorForm, FilialForm, VendedorForm, GrupoForm, ProdutoForm


# Create your views here.

# redicionamento de paginas

# Views referente ao CRUD dos CLIENTES
def home(request):
    return render(request, 'cadastros/index.html')


def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/clientes.html', {'clientes': clientes})


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
    if request.method == 'POST':
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


# Views referente ao CRUD dos FORNECEDORES
def list_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores.html', {'fornecedores': fornecedores})


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
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('list_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
        return render(request, 'cadastros/fornecedores_cadastro.html', {'form':form})
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores.html', {'fornecedores': fornecedores})


def delete_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    return redirect('list_fornecedores')


# Views referente ao CRUD das Filiais
def list_filiais(request):
    filiais = Filial.objects.all()
    return render(request, 'cadastros/filiais.html', {'filiais': filiais})


def new_filial(request):
    if request.method == 'POST':
        form = FilialForm(request.POST)
        if form.is_valid():
            form.save()
            filiais = Filial.objects.all()
            return redirect('list_filiais')
    else:
        form = FilialForm()
        return render(request, 'cadastros/filiais_cadastro.html', {'form':form})
    filiais = Filial.objects.all()
    return render(request, 'cadastros/filiais.html', {'filiais': filiais})


def edit_filial(request, pk):
    filial = get_object_or_404(Filial, pk=pk)
    if request.method == 'POST':
        form = FilialForm(request.POST, instance=filial)
        if form.is_valid():
            form.save()
            return redirect('list_filiais')
    else:
        form = FilialForm(instance=filial)
        return render(request, 'cadastros/filiais_cadastro.html', {'form':form})
    filiais = Filial.objects.all()
    return render(request, 'cadastros/filiais.html', {'filiais':filiais})

def delete_filial(request, pk):
    filial = get_object_or_404(Filial, pk=pk)
    filial.delete()
    return redirect('list_filiais')


# Views referente ao CRUD dos Vendedores
def list_vendedores(request):
    vendeores = Vendedor.objects.all()
    return render(request, 'cadastros/vendedores.html', {'vendedores':vendeores})


def new_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            vendedores = Vendedor.objects.all()
            return redirect('list_vendedores')
    else:
        form = VendedorForm()
        return render(request, 'cadastros/vendedores_cadastro.html', {'form':form})
    vendedores = Vendedor.object.all()
    return render(request, 'cadastros/vendedores.html', {'vendedores':vendedores})

def edit_vendedor(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('list_vendedores')
    else:
        form = VendedorForm(instance=vendedor)
        return render(request, 'cadastros/vendedores_cadastro.html', {'form': form})
    vendedores = Vendedor.objects.all()
    return render(request, 'cadastros/vendedores.html', {'vendedores':vendedores})


def delete_vendedor(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    vendedor.delete()
    return redirect('list_vendedores')

# Views referente ao CRUD dos Grupos de Produtos
def list_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'cadastros/grupos.html', {'grupos':grupos})


def new_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            grupos = Grupo.objects.all()
            return redirect('list_grupos')
    else:
        form = GrupoForm()
        return render(request, 'cadastros/grupos_cadastro.html', {'form':form})
    grupos = Grupo.objects.all()
    return render(request, 'cadastros/grupos.html', {'grupos':grupos})


def edit_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('list_grupos')
    else:
        form = GrupoForm(instance=grupo)
        return render(request, 'cadastros/grupos_cadastro.html', {'form':form})
    grupos = Grupo.objects.all()
    return render(request, 'cadastros/grupos.html', {'grupos':grupos})

def delete_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    grupo.delete()
    return redirect('list_grupos')

# Views referente ao CRUD dos Vendedores
def list_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'cadastros/produtos.html', {'produtos':produtos})

def new_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            produtos = Produto.objects.all()
            return redirect('list_produtos')
    else:
        form = ProdutoForm()
        return render(request, 'cadastros/produtos_cadastro.html', {'form':form})
    grupos = Grupos.objects.all()
    return render(request, 'cadastros/produtos.html', {'produtos':produtos})

def edit_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('list_produtos')
    else:
        form = ProdutoForm(instance=produto)
        return render(request, 'cadastros/produtos_cadastro.html', {'form':form})
    produtos = Grupo.objects.all()
    return render(request, 'cadastros/produtos.html', {'produtos':produtos})


def delete_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('list_produtos')




































