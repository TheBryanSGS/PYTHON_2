--
-- Resticciones a la Tabla: Empleados
--
ALTER TABLE Empleados ADD CONSTRAINT ch_Empleados_Valid_Numer   CHECK (Cedula > 1000000 AND Salario_Base >= 1160000 AND Hijos >= 0);
ALTER TABLE Empleados ADD CONSTRAINT ch_Empleados_Estado_Civil  CHECK (Estado_Civil IN ('S', 'C', 'U', 'P', 'D', 'V'));
ALTER TABLE Empleados ADD CONSTRAINT ch_Empleados_Nacimiento    CHECK (Nacimiento    <= CURRENT_DATE - interval '18 years');
ALTER TABLE Empleados ADD CONSTRAINT ch_Empleados_Fecha_Ingreso CHECK (Fecha_Ingreso <= CURRENT_DATE);