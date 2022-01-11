from typing import ContextManager
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def moneda(request):
    num = 1
    context = {'num' : num}
    return render(request, 'hola/moneda.html', context)

# ============ Estaticas ============
def hola(request):
    return render(request, 'hola/index.html')

# def vader(request):
#     return HttpResponse("Hola, Darth Vader")

# def starwars(request):
#     return HttpResponse("Hola StartWars")

# ============ Dinamicas ============
# def saludo(request, nombre):
#     return HttpResponse(f"Hola {nombre}!!!")

def saludo(request, nombre):
    context = {'name': nombre}
    return render(request, 'hola/saludo.html', context)


