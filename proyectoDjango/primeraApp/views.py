from django.shortcuts import render

# Create your views here.

# Deben ser funciones las vistas
def vista(peticion):
    return render(peticion, 'primeraApp.html')