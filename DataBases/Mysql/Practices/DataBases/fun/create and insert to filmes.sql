create database if not exists fun
default character set utf8
default collate utf8_general_ci;

CREATE TABLE filmes (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(55),
    Ano_de_Producao INT,
    Avaliacao DOUBLE
);

INSERT INTO filmes (Nome, Ano_de_Producao, Avaliacao) VALUES
('Interstellar', 2014, 9.2),
('The Shawshank Redemption', 1994, 9.3),
('Inception', 2010, 8.8),
('The Godfather', 1972, 9.2),
('Pulp Fiction', 1994, 8.9),
('The Dark Knight', 2008, 9.0),
('Forrest Gump', 1994, 8.8),
('Schindler''s List', 1993, 8.9),
('Fight Club', 1999, 8.8),
('The Matrix', 1999, 8.7);

select * from filmes;