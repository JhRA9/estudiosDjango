from django.shortcuts import render

# Create your views here.


# Deben ser funciones las vistas
def vista(peticion):
    lista_carros = {"titulo": "BWM"}, {"titulo": "lambo"}
    contexto = {"lista_carros": lista_carros}
    return render(peticion, "primeraApp.html", contexto)
