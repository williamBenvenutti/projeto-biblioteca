from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Pessoa, Livro
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

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
            return render(request, 'pagina-inicial.html', {'username': username})
        else:
            return HttpResponse('Credenciais Inválidas!')

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
            return HttpResponse('As senhas não são iguais')

        if users.exists():
            return HttpResponse('Já existe um usuário com esse username')
        elif emails.exists():
            return HttpResponse('Já existe um usuário com este email')
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(senha)
            user.save()
            return render(request, 'login.html')
        
def VerPessoas(request):
    pessoa = Pessoa.object.all()
    return render(request, 'pessoas_registradas.html', {"pessoa": pessoa})

def CriarPessoas(request):
    if request.method == "POST":
        new_nome = request.POST.get('nome')
        new_email = request.POST.get('email')
        new_telefone = request.POST.get('telefone')
        new_cpf = request.POST.get('cpf')
        new_rua = request.POST.get('rua')
        new_bairro = request.POST.get('bairro')
        new_numero = request.POST.get('numero')

        valida_cpf = Pessoa.objects.filter(cpf = valida_cpf)

        if valida_cpf.exists:
            return HttpResponse('CPF já cadastrado!')

        Pessoa.objects.create(
            nome=new_nome, email=new_email, telefone=new_telefone, cpf=new_cpf, rua=new_rua, bairro=new_bairro, numero=new_numero
        )
        return HttpResponse('Pessoa cadastrada!')
    else:
        return render(request, 'cadastro_pessoas.html')
    
def CriarLivros(request):
    if request.method == 'POST':
        new_titulo = request.POST.get('titulo')
        new_autor = request.POST.get('autor')
        new_editora = request.POST.get('editora')
        new_data_lancamento = request.POST.get('data_lancamento')
        new_genero = request.POST.get('genero')
        new_idioma = request.POST.get('idioma')
        Livro.objects.create(
            titulo = new_titulo, autor = new_autor, editora = new_editora, data_lancamento = new_data_lancamento, genero = new_genero, idioma = new_idioma
        )
        livros = Livro.objects.all()
        return redirect('mostra_livro')
    else:
        return render(request, 'cadastro_livros.html')
    
def MostrarLivros(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        livros = Livro.objects.filter(titulo__icontains=pesquisa)
    else:
        livros = Livro.objects.all()

    return render(request, 'mostra_livros.html', {'livros': livros})

def RealizarEmprestimo(request):
    pass
        