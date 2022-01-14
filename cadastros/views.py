from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

# redicionamento de paginas


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
        form = ClienteForm(request.POST, instance=cliente)
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