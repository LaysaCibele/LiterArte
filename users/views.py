from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CadastroForm
from .models import Perfil

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            novo_usuario = User.objects.create_user(username=email, email=email, password=senha)
            novo_usuario.first_name = nome
            novo_usuario.save()
            
            Perfil.objects.create(usuario=novo_usuario)
            
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})