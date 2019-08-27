from django.shortcuts import render

# Create your views here.


def retornar_index(request):

    return render(request, 'index.html')

def sobre(request):
    salada_de_frutas = ['banana', 'mamao', 'kiwi', 'abacate']

    contexto = {
        'salada_de_frutas' : salada_de_frutas
    }
    return render(request,'sobre.html', contexto)