--
-- Secuencia: s_auditoria
--
-- DROP SEQUENCE IF EXISTS s_auditoria;

CREATE SEQUENCE IF NOT EXISTS s_auditoria
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9999999
    ;

ALTER SEQUENCE s_auditoria
    OWNER TO postgres;