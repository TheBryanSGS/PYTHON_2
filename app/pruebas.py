import psycopg2
import bcrypt
from passlib.hash import bcrypt
from datetime import datetime

class ConextionDB:
    #--
    user = ''
    #--
    def __init__(self):
        #--
        try:
            #--
            self.__conextion = psycopg2.connect(
                database = 'DB_SCAHL',
                user = 'postgres',
                password = 'Santiago123.',
                port = '5432')
            self.__cursor = self.__conextion.cursor()
            #--
        except Exception as Ex: f"Ocurrio un ERROR: {Ex}"
        #--
    #--
    #Metodo que valida el inicio de sesion con usuario y contrasena
    #--
    def iniciar_Sesion(self, usuario, contrasena):
        #--
        try:
            #--
            sql = "SELECT contrasena "\
                    "FROM usuarios "\
                   "WHERE nombre = '" + str(usuario) + "'"
            self.__cursor.execute(sql)
            validar_contrasena = self.__cursor.fetchone()
            #--
            if validar_contrasena is not None:
                #--
                if bcrypt.verify(contrasena, validar_contrasena[0].encode()):
                    self.user = usuario
                    return "Acceso exitoso"
                #--
            #--
            return "Usuario y/o contraseña invalidos"
            #--
        except Exception as Ex: return f"Ocurrio un ERROR: {Ex}"
    #--
    #Metodo que permite realizar el registro de un empleado que entro a las instalaciones
    #--
    def empleado_Ingresa(self, cedula):
        #--
        try:
            #--
            existe = self.validar_Existencia(cedula)
            #--
            if existe is not None and type(existe) is tuple:
                #--
                #Si el empleado no esta en las instalaciones, insertelo
                #--
                asiste = self.validar_Asistencia(cedula)
                #--
                if asiste is None:
                    #--
                    sql = "INSERT INTO Asistencia_Empleados ("\
                              "Cedula"\
                             ",Salida"\
                             ",Usua_Cre"\
                          ") VALUES ("\
                             + str(cedula)\
                           + ",NULL"\
                           + ",'" + self.user + "')"
                    #--
                    self.__cursor.execute(sql)
                    self.__conextion.commit()
                    return "Empleado registrado correctamente"
                    #--
                elif asiste is not None and type(asiste) is tuple: return f"El empleado con numero de cedula '{cedula}' ya ingreso a las instalaciones"
                else: return f"ERROR en Valida_Asistencia:\n{asiste}"
                #--
            elif existe is None: return f"El empleado con numero de cedula '{cedula}' no existe"
            else: return f"ERROR en Valida_Existencia:\n{existe}"
            #--
        except Exception as Ex: f"ERROR en Empleado_Ingresa: {Ex}"
        #--
    #--
    #Metodo que permite realizar el registro de un empleado que sale de las instalaciones
    #--
    def empleado_Sale(self, cedula):
        #--
        try:
            #--
            existe = self.validar_Existencia(cedula)
            #--
            if existe is not None and type(existe) is tuple:
                #--
                #Si el empleado esta en las instalaciones, actualicelo
                #--
                asiste = self.validar_Asistencia(cedula)
                #--
                if asiste is not None and type(asiste) is tuple:
                    #--
                    horas_Extra = self.validar_Horas_Extra(cedula)
                    #--
                    if type(horas_Extra) is not str:
                        #--
                        sql = "UPDATE Asistencia_Empleados "\
                                 "SET horas_ex = " + str(horas_Extra) +\
                                    ",Salida = CURRENT_TIMESTAMP"\
                                    ",usua_mod = '" + self.user + "'"\
                              " WHERE Cedula = "+ str(cedula) +\
                                " AND Salida IS NULL"
                        #--
                        self.__cursor.execute(sql)
                        self.__conextion.commit()
                        #--
                        return "Empleado registrado correctamente" + (f"\nAdemas, realizo {horas_Extra} horas extra, por favor notificar" if horas_Extra > 0 else "")
                        #--
                    else: return f"ERROR en validar_Horas_Extra:\n{horas_Extra}"
                    #--
                elif asiste is None: return f"El empleado con numero de cedula '{cedula}' no ha ingresado"
                else: f"ERROR en Valida_Asistencia:\n{asiste}"
                #--
            elif existe is None: return f"El empleado con numero de cedula '{cedula}' no existe"
            else: return f"ERROR en Valida_Existencia:\n{existe}"
            #--
        except Exception as Ex: return f"ERROR en empleado_Sale: {Ex}"
        #--
    #--
    #Metodo que permite generar la consulta de un reporte para exportarlo a un archivo csv
    #--
    def generar_Reporte(self, fecha_ini, fecha_fin):
        #--
        try:
            #--
            str_fecha_ini = fecha_ini.strftime("%Y-%m-%d")
            str_fecha_fin = fecha_fin.strftime("%Y-%m-%d")
            #--
            sql = "SELECT cedula, nombre_completo, cargo, area, TO_CHAR(ingreso, 'DD-MM-YYYY HH:MI AM'), TO_CHAR(salida, 'DD-MM-YYYY HH:MI AM'), horas_extra "\
                    "FROM v_registro_asistencias "\
                   "WHERE ingreso BETWEEN TO_DATE('" + str_fecha_ini + "', 'YYYY-MM-DD') AND TO_DATE('" + str_fecha_fin + "', 'YYYY-MM-DD') + INTERVAL '1 day'"\
                    "  OR salida  BETWEEN TO_DATE('" + str_fecha_ini + "', 'YYYY-MM-DD') AND TO_DATE('" + str_fecha_fin + "', 'YYYY-MM-DD') + INTERVAL '1 day'"
            self.__cursor.execute(sql)
            return [(';'.join(map(lambda x: str(x) if x is not None else " ",fila))) for fila in self.__cursor.fetchall()]
            #--
        except Exception as Ex: return f"ERROR en consultar_Reporte{Ex}"
        #--
    #--
    #Metodo que valida la existencia de un empleado en la empresa por medio de su cedula
    #--
    def validar_Existencia(self, cedula):
        #--
        try:
            #--
            sql = 'SELECT 1 '\
                    'FROM Empleados '\
                   "WHERE Cedula = " + str(cedula)
            self.__cursor.execute(sql)
            return self.__cursor.fetchone()
            #--
        except Exception as Ex: return f"Ocurrio un ERROR: {Ex}"
        #--
    #--
    #Metodo que valida la asistencia de un empleado en la empresa por medio de su cedula
    #--
    def validar_Asistencia(self, cedula):
        #--
        try:
            #--
            sql = 'SELECT 1 '\
                    'FROM Asistencia_Empleados '\
                   'WHERE Cedula = ' + str(cedula) +\
                    ' AND Salida IS NULL'
            self.__cursor.execute(sql)
            return self.__cursor.fetchone()
            #--
        except Exception as Ex: return f"Ocurrio un ERROR: {Ex}" 
        #--
    #--
    #Metodo que calcula el numero de horas extra del empleado
    #--
    def validar_Horas_Extra(self, cedula):
        #--
        #Esta consulta recupera el numero de horas diarias laborales de un empleado dependiendo
        #del dia en el cual se haya asistido, ya que los empleados pueden variar en sus horas
        #laborales en el transcurso de la semana
        #--
        try:
            #--
            dia_semana = datetime.now().weekday() + 1
            sql = "SELECT COALESCE(Horas_Diarias[" + str(dia_semana) + "], 0) "\
                    "FROM Empleados "\
                   "WHERE Cedula = " + str(cedula)
            self.__cursor.execute(sql)
            hora_laboral = self.__cursor.fetchone()[0]
            #--
            #Consulta la cual trae el calculo de las horas extra
            #--
            sql = "SELECT EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - Ingreso)) / 3600 "\
                    "FROM Asistencia_Empleados "\
                   "WHERE Cedula = " + str(cedula) +\
                    " AND Salida IS NULL"
            self.__cursor.execute(sql)
            horas_realizadas = round(self.__cursor.fetchone()[0])
            #--
            #Si las horas realizadas son mayores a las horas laborales realizadas, retornar el numero de
            #horas extra
            return (horas_realizadas - hora_laboral) if horas_realizadas > hora_laboral else 0
            #--
        except Exception as Ex: return f"Ocurrio un ERROR: {Ex}"
    #--
    #Valida los permisos de un usuario para generar reportes
    #--
    def validar_Permisos(self):
        #--
        try:
            #--
            sql = "SELECT 1 "\
                    "FROM usuarios "\
                   "WHERE nombre = '" + self.user + "' "\
                     "AND 'GR' = ANY(permisos)"
            self.__cursor.execute(sql)
            return self.__cursor.fetchone()
            #--
        except Exception as Ex: return f"Ocurrio un ERROR: {Ex}"
        #--
    #--
    def __del__(self):
        #--
        self.__cursor.close()
        self.__conextion.close()
        #--
    #--
#--