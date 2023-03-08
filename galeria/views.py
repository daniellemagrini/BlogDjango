from django.shortcuts import render


def index(request): #Responsável pela página principal
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

