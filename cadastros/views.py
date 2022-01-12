from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

# redicionamento de paginas
def home(request):
    return render(request, 'cadastros/index.html')

def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/clientes.html', {'clientes': clientes})

def new_cliente(request):
    if request.method == "POST":
        form = ClienteForm()
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
    else:
        form = ClienteForm()
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/index.html')
