from django.urls import path
from .views import Login, CriarUsuario, CriarPessoas, CriarLivros, MostrarLivros

urlpatterns = [
    path("", Login, name='logar'),
    path('cadastro/', CriarUsuario,name='cadastro'),
    path('cadastro_pessoa/', CriarPessoas,name='cadastro_pessoa'),
    path('cadastro_livro/', CriarLivros,name='cadastro_livro'),
    path('mostra_livro/', MostrarLivros, name='mostra_livro')
]