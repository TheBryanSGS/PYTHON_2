--
-- Resticciones a la Tabla: Auditoria
--
ALTER TABLE Auditoria ADD CONSTRAINT fk_Auditoria_Id_Usuario FOREIGN KEY (Id_Usuario) REFERENCES Usuarios(Nombre);