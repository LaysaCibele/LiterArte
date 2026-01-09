from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CadastroForm
from .models import Perfil
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.first_name}!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, 'Você saiu da conta.')
    return redirect('login')