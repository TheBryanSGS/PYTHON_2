from pruebas import ConextionDB
from datetime import datetime
import os
import openpyxl

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
        # Crear un nuevo libro de Excel
        libro_excel = openpyxl.Workbook()

        # Seleccionar la hoja activa (por defecto, hay una hoja llamada "Sheet")
        hoja_activa = libro_excel.active

        # Agregar encabezados a la hoja de trabajo
        hoja_activa.append(encabezados)

        # Escribir los registros en la hoja de Excel
        for fila in registros:
            hoja_activa.append(fila.split(';'))

        # Obtener el directorio de descargas del usuario
        directorio_descargas = os.path.expanduser("~\Downloads")

        # Concatenar la ruta del archivo
        ruta_archivo = os.path.join(directorio_descargas, 'Registro' + datetime.now().strftime("%Y-%m-%d") + '.xlsx')

        # Guardar el libro de Excel en el directorio de descargas
        libro_excel.save(ruta_archivo)
        #--
        return "Archivo Excel generado con exito"
        #--
    except Exception as Ex: return f"ERROR en generar_Excel:\n{Ex}"
#--
instanciaDB = ConextionDB()
#--
try:
    #--
    USER = input("Ingrese el usuario\n")
    PSWD = input("Ingrese la contraseña\n").encode()
    acceso = instanciaDB.iniciar_Sesion(USER, PSWD)
    #--
    if acceso == "Acceso exitoso":
        #--
        print(acceso)
        opcion = ""
        #--
        while opcion != "3":
            #--
            print("Disque los botones:",
                  "1. Ingresar empleado.",
                  "2. Generar reporte.",
                  "3. Salir",
                  sep = "\n")
            opcion = input()
            #--
            if opcion == "1":
                #--
                print("Disque los botones:",
                      "1. El empleado va a ingresar.",
                      "2. El empleado va a salir.",
                      "3. Cancelar",
                      sep = "\n")
                opcion_1 = input()
                #--
                while opcion_1 not in ["1", "2", "3"]:
                    #--
                    opcion_1 = input("Ingrese segun el menu\n")
                    #--
                else:
                    #--
                    try:
                        #--
                        if opcion_1 == "1":
                            #--
                            cedula = int(input("Ingrese la cedula del empleado\n"))
                            print(instanciaDB.empleado_Ingresa(cedula, USER))
                            #--
                        elif opcion_1 == "2":
                            #--
                            cedula = int(input("Ingrese la cedula del empleado\n"))
                            print(instanciaDB.empleado_Sale(cedula, USER))
                            #--
                        else: print("Acaba de cancelar la operación")
                        #--
                    except ValueError: print("Formato de numero invalido")
                    #--
                #--
            elif opcion == "2":
                #--
                permisos = instanciaDB.validar_Permisos(USER)
                #--
                if permisos is not None and type(permisos) is tuple:
                    #--
                    print(generar_Excel(
                        instanciaDB.generar_Reporte(datetime(2023, 12, 11), datetime.now())
                        ))
                    #--
                elif permisos is None: print("Usted no tiene permisos para generar reportes")
                else: print(f"ERROR en validar_Permisos:\n{permisos}")
                #--
            elif opcion == "3":
                #--
                print("Gracias por usar la aplicación, buen dia")
                USER = None
                PSWD = None
                #--
            else: print("Escoja una opcion de la lista del menu por favor")
            #--
        #--
    else: print(acceso)
    #--
except Exception as Ex: print(f"Ocurrio un ERROR: {Ex}")
#--
instanciaDB.__del__()