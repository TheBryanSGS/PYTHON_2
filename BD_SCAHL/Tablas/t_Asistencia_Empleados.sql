--
-- Tabla: Asistencia_Empleados
--
-- DROP TABLE IF EXISTS Asistencia_Empleados;

CREATE TABLE IF NOT EXISTS Asistencia_Empleados
(
    Identif  NUMERIC(7,0)   DEFAULT    NEXTVAL('s_Asistencia_Empleados')
   ,Cedula   NUMERIC(11,0)  CONSTRAINT nn_Asistencia_Empleados_Cedula    NOT NULL
   ,Ingreso  TIMESTAMPTZ    DEFAULT    CURRENT_TIMESTAMP
   ,Salida   TIMESTAMPTZ    DEFAULT    CURRENT_TIMESTAMP
   ,Horas_Ex NUMERIC(2,0)   DEFAULT 0
   ,Usua_Cre VARCHAR(20)    CONSTRAINT nn_Asistencia_Empleados_Usua_Cre  NOT NULL
   ,Usua_Mod VARCHAR(20)
)
TABLESPACE pg_default;
--
ALTER TABLE IF EXISTS public.Asistencia_Empleados
    OWNER to postgres;
--
-- Comentarios de la tabla y de las columnas de cada tabla
--
COMMENT ON TABLE  Asistencia_Empleados          IS 'Registro de los empleados que ingresan a la empresa';
COMMENT ON COLUMN Asistencia_Empleados.Identif  IS 'Identificacion del registro en BD';
COMMENT ON COLUMN Asistencia_Empleados.Cedula   IS 'Cedula de un empleado';
COMMENT ON COLUMN Asistencia_Empleados.Ingreso  IS 'Ingreso de un empleado, representa la fecha de insercion del registro';
COMMENT ON COLUMN Asistencia_Empleados.Salida   IS 'Salida de un empleado, representa la fecha de modificacion del registro';
COMMENT ON COLUMN Asistencia_Empleados.Horas_Ex IS 'Horas Extra del empleado, si se llegan a reportar';
COMMENT ON COLUMN Asistencia_Empleados.Usua_Cre IS 'Usuario que creo el registro';
COMMENT ON COLUMN Asistencia_Empleados.Usua_Mod IS 'Usuario que modifico el registro';