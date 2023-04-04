CREATE TABLE pedido (
    id int auto_increment PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    cantidad    VARCHAR(255) NOT NULL UNIQUE,
    producto VARCHAR(255) NOT NULL UNIQUE,
    nombreProducto VARCHAR(255) NOT NULL UNIQUE,
    precio VARCHAR(255) NOT NULL
);

CREATE TABLE productos (
    id int auto_increment PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    img    VARCHAR(255),
    descripcion VARCHAR(255),
    precio VARCHAR(255),
    categoria VARCHAR(255)
);


CREATE DATABASE localTeteria;
CREATE USER 'localTeteria'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON localTeteria.* TO 'localTeteria'@'localhost' WITH GRANT OPTION;


INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Kit cachimba iniciacion', './../IMG/iniciacion.jpg', 'KIT CACHIMBA INICIACIÓN de KAYA SHISHA. Este kit súper completo es ideal para los que quieran iniciarse en el mundo de la cachimba pero no saben muy bien qué elegir. ¡Viene con todos los accesorios indispensables para la elaboración de la shisha!', '50', 'CACHIMBAS');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Kit cachimba travel', './../IMG/travel.jpg', 'KIT CACHIMBA TRAVEL Este fantástico kit tiene todo lo que necesitas para disfrutar de la cachimba. Incluye la cachimba Kaya ELOX, una shisha de aluminio anodizado con un atractivo diseño y que trae consigo una base con forma de reloj de arena', '60', 'CACHIMBAS');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Cachimba lite', './../IMG/lite.jpg', 'El modelo LITE es la shisha más popular de la marca, de diseño austero y materiales de alta calidad, y con un punto fuerte a destacar, su rendimiento. Ademas tiene el mastil intercambiable hasta con 4 modelos diferentes', '100', 'CACHIMBAS');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Hibou Tropic', './../IMG/hibou.png', 'Vodka, melocotón, piña, granadina y blue curaçao', '7', 'COCTELES');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Hawaian Sommer', './../IMG/summer.png', 'Vodka, ron, piña, arándanos, sandía y fruta de la pasión ', '7', 'COCTELES');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Daikiri', './../IMG/daikiri.png', 'Ron, lima y azúcar', '7', 'COCTELES');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Piña Colada', './../IMG/piña.png', 'Ron, piña, naranja, coco y triple sec.', '7', 'COCTELES');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('XL', './../IMG/xl.png', '¡Elige tu coctel preferido y disfrútalo a lo grande!', '30', 'COCTELES');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Nachos', './../IMG/nachos.avif', '¡Elige tu salsa favorita queso o guacamole!', '7', 'MERIENDAS');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Panini', './../IMG/panini.jpg', '¡Elige tu panini con los toppings que quieras!', '8', 'MERIENDAS');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Pizza', './../IMG/pizza.avif', '¡Elige tu pizza entre barbacoa, jamon y queso o cuatro quesos !', '10', 'MERIENDAS');

INSERT INTO productos (nombre, img, descripcion, precio, categoria)
    VALUES ('Tortitas', './../IMG/tortitas.jpeg', '¡Elige tus tortitas con nata o sirope del sabor que prefieras!', '8', 'MERIENDAS');

    
