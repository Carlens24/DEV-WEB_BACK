-- Criação de um novo banco de dados chamado "tst"
CREATE DATABASE tst;

-- Criação de uma tabela chamada "tstinfo" com três colunas: id, nome e descrição
CREATE TABLE tstinfo (
    id INT,
    nome VARCHAR(20),
    descricao TEXT
);

-- Inserção de dados na tabela "tstinfo"
INSERT INTO tstinfo (id, nome, descricao) VALUES
('1', 'Carlens oslin', 'Artista e programador iniciante'),
('2', 'Schneidine oslin', 'Artista, programadora e marombeira'),
('3', 'Darley oslin', 'Bêbê brabo!!');

-- Desativação do modo de confirmação automática para que as transações sejam controladas manualmente
SET autocommit = OFF;

-- Criação de um ponto de salvamento (commit) para confirmar as alterações feitas até agora
COMMIT;

-- Tentativa de exclusão de todas as linhas da tabela "tstinfo"
-- (Isso não será confirmado automaticamente devido ao autocommit desativado)
DELETE FROM tstinfo;

-- Rollback para reverter todas as alterações desde o último ponto de salvamento (commit)
ROLLBACK;

-- Seleção de todas as linhas da tabela "tstinfo" para verificar o estado atual dos dados
SELECT * FROM tstinfo;
