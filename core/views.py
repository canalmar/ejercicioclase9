from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Django! yeahhhh")

def saludar_con_etiqueta(resquest):
    return HttpResponse("<h1>HOLA</h1")

def saludar_con_parametros(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido=apellido.upper()
    return HttpResponse(f"Hola desde Django! yeahhhh, {nombre} {apellido}")

def index(request):
    datos = {
        "nombre": "vero",
        "rol": "tutora",
    }
    return render(request, "core/index.html", context=datos)