from django.shortcuts import render, redirect
from .pruebas import ConextionDB
from django.contrib import messages

conexion = ConextionDB()

def index(request):
    return render(request, 'index.html')
def opciones(request):
    return render(request, 'opciones.html')
def reporte (request):
    return render(request, 'reporte.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        resultado = conexion.iniciar_Sesion(username, password)

        if resultado == "Acceso exitoso":
            return redirect('opciones')
        else:
            messages.error(request, resultado)

    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
    
        if 'btn-entrada' in request.POST:
            validar_ingreso = conexion.empleado_Ingresa(cedula)
        elif 'btn-salida' in request.POST:
            validar_ingreso = conexion.empleado_Sale(cedula)
        else:
            return redirect('registro')
        
        print(validar_ingreso)

    return render(request, 'registro.html')