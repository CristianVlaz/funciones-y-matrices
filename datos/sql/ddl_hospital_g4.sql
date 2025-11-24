
-- CREATE DATABASE IF NOT EXISTS hospital_g4;

-- -- 2. Le dice a MySQL que use esta base de datos para los siguientes comandos.
-- USE hospital_g4;

-- -- 3. Tabla de Especialidades
-- -- (Requerida por los Doctores)
-- CREATE TABLE IF NOT EXISTS especialidades (
--     id INT AUTO_INCREMENT,
--     nombre_especialidad VARCHAR(100) NOT NULL UNIQUE,
--     descripcion TEXT NULL,
--     habilitado TINYINT NOT NULL DEFAULT 1,

--     CONSTRAINT pk_especialidades PRIMARY KEY (id)
-- );

-- -- 4. Tabla de Doctores
-- -- (Requerida por las Citas)
-- CREATE TABLE IF NOT EXISTS doctores (
--     id INT AUTO_INCREMENT,
--     rut_doctor CHAR(10) NOT NULL UNIQUE,
--     nombre_doctor VARCHAR(150) NOT NULL,
--     id_especialidad INT NOT NULL,
--     habilitado TINYINT NOT NULL DEFAULT 1,

--     CONSTRAINT pk_doctores PRIMARY KEY (id),
--     CONSTRAINT fk_doctores_especialidades FOREIGN KEY (id_especialidad) REFERENCES especialidades(id)
-- );

-- -- 5. Tabla de Pacientes
-- -- (Requerida por las Citas)
-- CREATE TABLE IF NOT EXISTS pacientes (
--     id INT AUTO_INCREMENT,
--     rut_paciente CHAR(10) NOT NULL UNIQUE,
--     nombre_paciente VARCHAR(150) NOT NULL,
--     fecha_nacimiento DATE NULL,
--     telefono VARCHAR(12) NULL,
--     historia_clinica TEXT NULL, -- Requisito del proyecto
--     habilitado TINYINT NOT NULL DEFAULT 1,

--     CONSTRAINT pk_pacientes PRIMARY KEY (id)
-- );

-- -- 6. Tabla de Citas
-- -- (Conecta Pacientes y Doctores)
-- CREATE TABLE IF NOT EXISTS citas (
--     id INT AUTO_INCREMENT,
--     fecha_cita DATE NOT NULL,
--     hora_cita TIME NOT NULL,
--     motivo_cita VARCHAR(255) NOT NULL,
--     id_paciente INT NOT NULL, -- FK a pacientes
--     id_doctor INT NOT NULL,   -- FK a doctores
--     habilitado TINYINT NOT NULL DEFAULT 1,

--     CONSTRAINT pk_citas PRIMARY KEY (id),
--     CONSTRAINT fk_citas_pacientes FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
--     CONSTRAINT fk_citas_doctores FOREIGN KEY (id_doctor) REFERENCES doctores(id)
-- );

-- -- 7. Tabla de Recetas
-- -- (Conectada a las Citas)
-- CREATE TABLE IF NOT EXISTS recetas (
--     id INT AUTO_INCREMENT,
--     id_cita INT NOT NULL, -- FK a citas
--     medicamentos TEXT NULL,
--     instrucciones TEXT NULL,
--     fecha_emision DATE NOT NULL,
--     habilitado TINYINT NOT NULL DEFAULT 1,

--     CONSTRAINT pk_recetas PRIMARY KEY (id),
--     CONSTRAINT fk_recetas_citas FOREIGN KEY (id_cita) REFERENCES citas(id)
-- );

-- resumen: Este script SQL crea la base de datos "hospital_g4" y define las tablas necesarias para gestionar especialidades, doctores, pacientes, citas y recetas.