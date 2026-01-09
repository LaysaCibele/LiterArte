from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'CampoNome', 'placeholder': 'Seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'CampoEmail', 'placeholder': 'seu@email.com'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'CampoSenha'}))
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'CampoConfirmarSenha'}))
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")
        email = cleaned_data.get("email")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está cadastrado.")
            
        if User.objects.filter(username=email).exists():
             raise forms.ValidationError("Este usuário já existe.")

        return cleaned_data