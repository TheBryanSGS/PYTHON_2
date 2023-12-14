--
-- Tabla: Usuarios
--
-- DROP TABLE IF EXISTS Usuarios;

CREATE TABLE IF NOT EXISTS Usuarios
(
    Nombre        VARCHAR(20)  CONSTRAINT nn_Usuarios_Nombre     NOT NULL
   ,Contrasena    TEXT         CONSTRAINT nn_Usuarios_Contraseña NOT NULL
   ,Permisos      VARCHAR(2)[] CONSTRAINT nn_Usuarios_Contraseña NOT NULL
   ,Activo        BOOLEAN      DEFAULT    true
   ,Fech_Reg      DATE         DEFAULT    CURRENT_DATE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS Usuarios
    OWNER to postgres;

COMMENT ON TABLE  Usuarios               IS 'Registro de los Usuarios';
COMMENT ON COLUMN Usuarios.Nombre        IS 'Nombre de usuario asignado';
COMMENT ON COLUMN Usuarios.Contrasena    IS 'Contraseña cifrada';
COMMENT ON COLUMN Usuarios.Permisos      IS 'Codigo de lista de permisos de los usuarios';
COMMENT ON COLUMN Usuarios.Activo        IS 'Usuario activo?';
COMMENT ON COLUMN Usuarios.Fech_Reg      IS 'Fecha de creacion del usuario';