USE cadastro;
# CREATE DATABASE cadastro
# DEFAULT CHARACTER SET UTF8
# DEFAULT COLLATE UTF8_GENERAL_CI;

CREATE table if not exists pessoas(
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR (30) NOT NULL,
nascimento DATE,
genero ENUM('F','M'),
peso DECIMAL (5, 2),
altura DECIMAL (3, 2),
nacionalidade VARCHAR(20) DEFAULT 'Brasil',
PRIMARY KEY (id)
) DEFAULT CHARSET = UTF8; 