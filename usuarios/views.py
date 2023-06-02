from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Pessoa
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class CadastrarUsuarioForm(forms.Form):
    nome_usuario = forms.CharField(max_length=35)
    email = forms.EmailField(max_length=100)
    senha = forms.CharField(min_length=8)
    confirmar_senha = forms.CharField(min_length=8)
    

def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'login.html')
        if user.check_password(password):
            return render(request, 'pagina-inicial.html')
        else:
            return render(request, 'login.html')


def CriarUsuario(request):
    if request.method == 'GET':
        return render(request, 'tela_cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')
        
        users = User.objects.filter(username=username)
        emails = User.objects.filter(email=email)

        if senha != confirma_senha:
            return HttpResponse('As senhs não são iguais')

        if users.exists():
            return HttpResponse("Já existe um usuário com esse username")
        elif emails.exists():
            return HttpResponse("Já existe um usuário com este email")
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(senha)
            user.save()

            return HttpResponse("Usuário criado com sucesso!")
