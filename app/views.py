from django.shortcuts import render, redirect
from .pruebas import ConextionDB
from django.contrib import messages
from datetime import datetime
import os
import openpyxl

conexion = ConextionDB()

def generar_Excel(registros):
    #--
    try:
        #--
        encabezados = [ 
            'Cedula'
           ,'Nombre Completo'
           ,'Cargo'
           ,'Area'
           ,'Fecha/Hora Ingreso'
           ,'Fecha/Hora Salida'
           ,'Horas Extra'
        ]
        #--
        libro_excel = openpyxl.Workbook()
        hoja_activa = libro_excel.active
        hoja_activa.append(encabezados)
        #--
        for fila in registros: hoja_activa.append(fila.split(';'))
        #--
        directorio_descargas = os.path.expanduser("~\Downloads")
        ruta_archivo = os.path.join(directorio_descargas, 'Registro' + datetime.now().strftime("%Y-%m-%d") + '.xlsx')
        libro_excel.save(ruta_archivo)
        #--
        return "Archivo Excel generado con exito"
        #--
    except Exception as Ex: return f"ERROR en generar_Excel:\n{Ex}"
    #--
#--

def index(request):
    return render(request, 'index.html')

def login(request):
    #--
    if request.method == 'POST':
        #--
        username = request.POST.get('username')
        password = request.POST.get('password')
        resultado = conexion.iniciar_Sesion(username, password)
        #--
        if resultado == "Acceso exitoso": return redirect('opciones')
        else: messages.error(request, resultado)
        #--
    return render(request, 'login.html')
    #--
#--
def opciones(request):
    #--
    if request.method == 'POST':
        #--
        if 'generareporte' in request.POST:
            #--
            validar_Permisos = conexion.validar_Permisos()
            #--
            if validar_Permisos is not None and type(validar_Permisos) is tuple: return redirect('reporte')
            else: messages.error(request, validar_Permisos)
            #--
        #--
    return render(request, 'opciones.html')
    #--
#--
def registro(request):
    #--
    if request.method == 'POST':
        #--
        cedula = request.POST.get('cedula')
        #--    
        if 'btn-entrada' in request.POST: validar_ingreso = conexion.empleado_Ingresa(cedula)
        elif 'btn-salida' in request.POST: validar_ingreso = conexion.empleado_Sale(cedula)
        else: return redirect('registro')
        #--
        print(validar_ingreso)
        #--
    return render(request, 'registro.html')
    #--
#--
def reporte (request):
    #--
    if request.method == 'POST':
        #--
        fecha_ini = request.POST.get('desde')
        fecha_fin = request.POST.get('hasta')
        #-- 
        genero_Archivo = generar_Excel(
                        conexion.generar_Reporte(datetime.strptime(fecha_ini, "%Y-%m-%d"),
                                datetime.strptime(fecha_fin, "%Y-%m-%d")
                            )
                        )
        #--
        print(genero_Archivo)
        #--
    #--
    return render(request, 'reporte.html')
#--