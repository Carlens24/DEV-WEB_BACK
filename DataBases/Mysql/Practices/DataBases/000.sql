CREATE DATABASE tutorial;

CREATE TABLE Filme(
    Nome VARCHAR(50),
    Ano_de_Producao INT,
    Avaliacao DOUBLE
);

INSERT INTO Filme(Nome, Ano_de_Producao, Avaliacao)
VALUES ('Rei Leao', 1998, 8.9);

SELECT * FROM Filme WHERE Nome = 'Rei Leao';
