CREATE TABLE grupos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    activo INT DEFAULT 1,
);
CREATE TABLE obreros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    telefono VARCHAR(255),
    direccion VARCHAR(255),
    id_grupo INT,
    activo INT DEFAULT 1,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id)
);
CREATE TABLE creyentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    telefono VARCHAR(255),
    direccion TEXT,
    dias_disp VARCHAR(255),
    id_grupo INT,
    activo INT DEFAULT 1,
    FOREIGN KEY (id_grupo) REFERENCES grupos(id)
);
CREATE TABLE estados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    activo INT DEFAULT 1,
);
CREATE TABLE problema (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_creyente INT,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    revision TIMESTAMP DEFAULT (CURRENT_TIMESTAMP + INTERVAL 1 WEEK),
    id_estado INT,
    activo INT DEFAULT 1,
    FOREIGN KEY (id_creyente) REFERENCES creyentes(id),
    FOREIGN KEY (id_estado) REFERENCES estados(id)
);
CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensaje TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_problema INT,
    activo INT DEFAULT 1,
    FOREIGN KEY (id_problema) REFERENCES problema(id)
);


/** vistas principales **/


CREATE VIEW vista_obreros AS
SELECT o.id, CONCAT(o.id, '-', o.nombre) AS id_nombre, o.telefono, o.direccion, CONCAT(g.id, '-', g.nombre) AS id_grupo, o.activo
FROM obreros o
JOIN grupos g ON o.id_grupo = g.id;

CREATE VIEW vista_creyentes AS
SELECT c.id, CONCAT(c.id, '-', c.nombre) AS id_nombre, c.telefono, c.direccion, c.dias_disp, CONCAT(g.id, '-', g.nombre) AS id_grupo, c.activo
FROM creyentes c
JOIN grupos g ON c.id_grupo = g.id;

CREATE VIEW vista_problema AS
SELECT p.id, CONCAT(c.id, '-', c.nombre) AS id_creyente, p.descripcion, CONCAT(e.id, '-', e.nombre) AS id_estado, p.activo
FROM problema p
JOIN creyentes c ON p.id_creyente = c.id
JOIN estados e ON p.id_estado = e.id
ORDER BY p.revision DESC;


CREATE VIEW vista_mensajes AS
SELECT m.id, m.mensaje, m.fecha, CONCAT(p.id, '-', p.descripcion) AS id_problema, m.activo
FROM mensajes m
JOIN problema p ON m.id_problema = p.id
ORDER BY m.fecha ASC; -- ASC para ordenar de forma ascendente (es decir, el más antiguo primero)



ALTER TABLE nombre_de_la_tabla
ADD correo VARCHAR(255),
ADD contrasena VARCHAR(255);