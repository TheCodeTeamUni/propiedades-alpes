CREATE TABLE usuarios(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    nombres VARCHAR(255),
    apellidos VARCHAR(255),
    direccion VARCHAR(255),
    telefono VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)

) COMMENT 'Tabla de usuarios';

CREATE TABLE contratos(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    id_propiedad int,
    monto FLOAT(10,2),
    vendedor VARCHAR(255),
    inquilino VARCHAR(255),
    arrendador VARCHAR(255)

) COMMENT 'Tabla de contratos';