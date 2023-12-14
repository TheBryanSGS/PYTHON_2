from django.shortcuts import render, redirect
from .pruebas import ConextionDB
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
def opciones(request):
    return render(request, 'opciones.html')
def registro (request):
    return render(request, 'registro.html')
def reporte (request):
    return render(request, 'reporte.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        conexion = ConextionDB()
        resultado = conexion.iniciar_Sesion(username, password)

        if resultado == "Acceso exitoso":
            return redirect('opciones')
        else:
            messages.error(request, resultado)

    return render(request, 'login.html')