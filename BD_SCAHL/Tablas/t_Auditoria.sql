--
-- Tabla: Auditoria
--
-- DROP TABLE IF EXISTS Auditoria;

CREATE TABLE IF NOT EXISTS Auditoria
(
    Identif    INTEGER      DEFAULT    NEXTVAL('s_Auditoria')
   ,Id_Usuario VARCHAR(20)  CONSTRAINT nn_Auditoria_Id_Usuario NOT NULL
   ,Tabla      VARCHAR(20)  CONSTRAINT nn_Auditoria_Tabla      NOT NULL
   ,Accion     VARCHAR(3)   CONSTRAINT nn_Auditoria_Accion     NOT NULL
   ,Info_Antes TEXT         CONSTRAINT nn_Auditoria_Info_Antes NOT NULL
   ,Info_Desp  TEXT         CONSTRAINT nn_Auditoria_Info_Desp  NOT NULL
   ,Fech_Reg   TIMESTAMPTZ  DEFAULT    CURRENT_TIMESTAMP
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS Auditoria
    OWNER to postgres;

COMMENT ON TABLE  Auditoria            IS 'Registro de las diferentes acciones realizadas a tablas en la BD';
COMMENT ON COLUMN Auditoria.Identif    IS 'Identificacion de la accion en la BD';
COMMENT ON COLUMN Auditoria.Id_Usuario IS 'Id del usuario que hizo la acción';
COMMENT ON COLUMN Auditoria.Tabla      IS 'Tabla a la cual afecto';
COMMENT ON COLUMN Auditoria.Accion     IS 'Si se hizo una insercion, actualizacion o eliminacion';
COMMENT ON COLUMN Auditoria.Info_Antes IS 'Informacion alterada antes de la acción';
COMMENT ON COLUMN Auditoria.Info_Desp  IS 'Informacion alterada despues de la accion';
COMMENT ON COLUMN Auditoria.Fech_Reg   IS 'Fecha de realizacion de la accion';