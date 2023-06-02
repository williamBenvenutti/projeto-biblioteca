from django.urls import path
from .views import Login, CriarUsuario

urlpatterns = [
    path("", Login, name='logar'),
    path('cadastro/', CriarUsuario,name='cadastro')
]