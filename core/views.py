from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def DomCasmurro(request):
    return render(request, 'DomCasmurro.html')

def editar_perfil(request):
    return render(request, 'editar-perfil.html')

def login(request):
    return render(request, 'login.html')

def meu_perfil(request):
    return render(request, 'meu-perfil.html')

def minha_lista(request):
    return render(request, 'minha-lista.html')