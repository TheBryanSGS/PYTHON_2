--
-- Secuencia: s_Asistencia_Empleados
--
-- DROP SEQUENCE IF EXISTS s_Asistencia_Empleados;

CREATE SEQUENCE IF NOT EXISTS ps_Asistencia_Empleados
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9999999
    ;

ALTER SEQUENCE s_Asistencia_Empleados
    OWNER TO postgres;