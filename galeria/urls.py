from django.urls import path
from galeria.views import index, imagem


urlpatterns = [
    path('', index, name='index.html'),
    path('imagem/', imagem, name='imagem.html'),
]