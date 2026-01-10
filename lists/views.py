from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from books.models import Livro
from .models import ListaLeitura
# Create your views here.

@login_required(login_url='login') 
def adicionar_na_lista(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    
    item, created = ListaLeitura.objects.get_or_create(
        usuario=request.user,
        livro=livro,
        defaults={'status': 'QUERO_LER'}
    )
    
    if created:
        messages.success(request, f'{livro.titulo} adicionado à sua lista!')
    else:
        messages.info(request, f'{livro.titulo} já está na sua lista.')
    
    return redirect('minha_lista')

@login_required(login_url='login')
def pagina_minha_lista(request):
    itens = ListaLeitura.objects.filter(usuario=request.user)
    return render(request, 'minha-lista.html', {'itens': itens})

