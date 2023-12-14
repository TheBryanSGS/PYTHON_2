--
-- Tabla: Empleados
--
-- DROP TABLE IF EXISTS Empleados;

CREATE TABLE IF NOT EXISTS Empleados
(
    Cedula        NUMERIC(11,0)  CONSTRAINT nn_Empleados_Cedula        NOT NULL
   ,Nombres       VARCHAR(30)    CONSTRAINT nn_Empleados_Nombres       NOT NULL
   ,Apellidos     VARCHAR(30)    CONSTRAINT nn_Empleados_Apellidos     NOT NULL
   ,Fecha_ingreso DATE           CONSTRAINT nn_Empleados_Fecha_Ingreso NOT NULL
   ,Cargo         VARCHAR(30)    CONSTRAINT nn_Empleados_Cargo         NOT NULL
   ,Area          VARCHAR(3)     CONSTRAINT nn_Empleados_Area          NOT NULL
   ,Horas_Diarias NUMERIC(2,0)[] CONSTRAINT nn_Empleados_Horas_Diarias NOT NULL
   ,Salario_Base  NUMERIC(11,2)  CONSTRAINT nn_Empleados_Salario_Base  NOT NULL
   ,Nacimiento    DATE           CONSTRAINT nn_Empleados_Nacimiento    NOT NULL
   ,Direccion     VARCHAR(30)    CONSTRAINT nn_Empleados_Direccion     NOT NULL
   ,Estado_Civil  VARCHAR(1)     CONSTRAINT nn_Empleados_Estado_Civil  NOT NULL
   ,Hijos         NUMERIC(2,0)   DEFAULT 0                                              
   ,Email         VARCHAR(40)    CONSTRAINT nn_Empleados_Email         NOT NULL
)
TABLESPACE pg_default;
--
ALTER TABLE IF EXISTS Empleados
    OWNER to postgres;
--
-- Comentarios de la tabla y de las columnas de cada tabla
--
COMMENT ON TABLE  Empleados               IS 'Generalización de una tabla que lleve el registro de los empleados en una empresa';
COMMENT ON COLUMN Empleados.Cedula        IS 'Cedula de un empleado';
COMMENT ON COLUMN Empleados.Nombres       IS 'Nombres de un empleado';
COMMENT ON COLUMN Empleados.Apellidos     IS 'Apellidos de un empleado';
COMMENT ON COLUMN Empleados.Fecha_ingreso IS 'Fecha de Ingreso a la empresa';
COMMENT ON COLUMN Empleados.Cargo         IS 'Cargo en la empresa';
COMMENT ON COLUMN Empleados.Area          IS 'Codigo de area en la que labora';
COMMENT ON COLUMN Empleados.Horas_Diarias IS 'Lista de horas que el empleado realiza a la semana';
COMMENT ON COLUMN Empleados.Salario_Base  IS 'Salario base del empleado';
COMMENT ON COLUMN Empleados.Nacimiento    IS 'Fecha de nacimiento del empleado';
COMMENT ON COLUMN Empleados.Direccion     IS 'Direccion del empleado';
COMMENT ON COLUMN Empleados.Estado_Civil  IS 'Codigo de estado civil: S-Soltero, C-Casado, U-Union libre, P-Separado, D-Divorciado, V-Viudo';
COMMENT ON COLUMN Empleados.Hijos         IS 'Numero de Hijos que tiene el empleado';
COMMENT ON COLUMN Empleados.Email         IS 'Correo electronico del empleado';