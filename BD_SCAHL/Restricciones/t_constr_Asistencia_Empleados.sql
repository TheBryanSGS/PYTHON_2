--
-- Resticciones a la Tabla: Asistencia_Empleados
--
ALTER TABLE Asistencia_Empleados ADD CONSTRAINT fk_Asistencia_Empleados_Usua_Ins FOREIGN KEY (Usua_Cre) REFERENCES Usuarios(Nombre);
ALTER TABLE Asistencia_Empleados ADD CONSTRAINT fk_Asistencia_Empleados_Usua_Mod FOREIGN KEY (Usua_Mod) REFERENCES Usuarios(Nombre);
ALTER TABLE Asistencia_Empleados ADD CONSTRAINT fk_Asistencia_Empleados_Cedula   FOREIGN KEY (Cedula)   REFERENCES Empleados(Cedula);
ALTER TABLE Asistencia_Empleados ADD CONSTRAINT ch_Asistencia_Empleados_Horario  CHECK (Ingreso < Salida);
ALTER TABLE Asistencia_Empleados ADD CONSTRAINT ch_Asistencia_Empleados_Horas_Ex CHECK (Horas_Ex >= 0);