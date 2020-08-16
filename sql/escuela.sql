USE lwlq4ui1z45n2fln;

CREATE TABLE IF NOT EXISTS alumnos(
id_alumno	     		INT(4)          	NOT NULL        AUTO_INCREMENT          PRIMARY KEY,
matricula               CHAR(10)            NOT NULL,
nombre           		VARCHAR(30)        NOT NULL,
apellido_paterno        VARCHAR(20)	        NOT NULL,
apellido_materno        VARCHAR(20)         NOT NULL,
edad                    CHAR(2)	            NOT NULL,
fecha_nacimiento        DATE,
sexo                    CHAR(10)            NOT NULL,
estado_civil            CHAR(10)            NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

/*INSERCION DE DOS ALUMNOS*/
INSERT INTO alumnos(id_alumno, matricula, nombre, apellido_paterno, apellido_materno, edad, fecha_nacimiento, sexo, estado_civil) VALUES 
(NULL, '1718110394', 'Andrea Sarai', 'Juárez', 'Munguia', '20', '2000/06/14', 'Femenino', 'Soltera');

INSERT INTO alumnos(id_alumno, matricula, nombre, apellido_paterno, apellido_materno, edad, fecha_nacimiento, sexo, estado_civil) VALUES 
(NULL, '1718110384', 'Julissa', 'Dominguez', 'Badillo', '20', '2000/04/05', 'Femenino', 'Soltera');

/*SELECT * FROM alumnos;
DELETE FROM alumnos WHERE id_alumno = "8";*/