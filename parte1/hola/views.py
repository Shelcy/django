from django.http.response import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# ============ Estaticas ============
def hola(request):
    return HttpResponse("Hola, mundo")

def vader(request):
    return HttpResponse("Hola, Darth Vader")

def starwars(request):
    return HttpResponse("Hola StartWars")

# ============ Dinamicas ============
def saludo(request, nombre):
    return HttpResponse(f"Hola {nombre}!!!")