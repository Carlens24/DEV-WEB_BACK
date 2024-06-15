-- Criação da Tabela USERS
CREATE TABLE USERS (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    FNAME VARCHAR(200) NOT NULL,
    LNAME VARCHAR(200) NOT NULL,
    EMAIL VARCHAR(200) UNIQUE NOT NULL, -- Corrigido para adicionar a coluna 'EMAIL' com o nome correto
    PASSW VARCHAR(200) NOT NULL,
    AGE INT
);

-- Selecionando Todos os Dados da Tabela USERS
SELECT * FROM USERS;

-- Função SUBSTRING
-- Extrai uma substring a partir da posição 7 com 5 caracteres
SELECT SUBSTRING('HELLO WORLD!', 7, 5);
-- Extrai uma substring a partir da posição 10 com 20 caracteres
SELECT SUBSTRING('LIFE IS A BULLSHIT LIKE IN THE BULLY HIGHSCHOOL GTA GAME!', 10, 20);
-- Extrai uma substring de LNAME a partir da posição 5
SELECT SUBSTRING(LNAME, 5) FROM USERS;

-- Função REPLACE
-- Substitui 'HELLO' por 'BYE' na string 'HELLO WORLD'
SELECT REPLACE('HELLO WORLD', 'HELLO', 'BYE');
-- Substitui 's' por 'S' na string 'sCHNEIdome'
SELECT REPLACE('sCHNEIdome', 's', 'S');
-- Substitui 'David' por 'TUDO CULPA DO Davidddd' no campo FNAME dos usuários
SELECT REPLACE(FNAME, 'David', 'TUDO CULPA DO Davidddd') FROM USERS;
-- Substitui 'Smith' por 'SMITHHH!' no campo LNAME dos usuários
SELECT REPLACE(LNAME, 'Smith', 'SMITHHH!') FROM USERS;

-- Função REVERSE
-- Reverte a string 'MAURO'
SELECT REVERSE('MAURO');
-- Reverte o campo FNAME dos usuários
SELECT REVERSE(FNAME) FROM USERS;
-- Reverte o campo PASSW dos usuários
SELECT REVERSE(PASSW) FROM USERS;

-- Função CHAR LENGTH, CHARACTER LENGTH ou LENGTH
-- Retorna o comprimento da string 'HELLO_WORLD'
SELECT CHAR_LENGTH('HELLO_WORLD');
-- Retorna o comprimento da string 'PARALELEPIPEDO'
SELECT CHARACTER_LENGTH('PARALELEPIPEDO');
-- Retorna o comprimento do campo LNAME dos usuários
SELECT CHAR_LENGTH(LNAME) FROM USERS;

-- Ordenação ORDER BY (DESC/ASC)
-- Ordena os primeiros nomes em ordem decrescente
SELECT FNAME FROM USERS ORDER BY FNAME DESC;
-- Ordena os primeiros nomes em ordem crescente
SELECT FNAME FROM USERS ORDER BY FNAME ASC;
-- Ordena os primeiros nomes pelo comprimento em ordem decrescente
SELECT FNAME FROM USERS ORDER BY LENGTH(FNAME) DESC;
-- Ordena os primeiros nomes pelo comprimento em ordem crescente
SELECT FNAME FROM USERS ORDER BY LENGTH(FNAME) ASC;

-- Limitar Resultados LIMIT
-- Seleciona os 5 primeiros sobrenomes em ordem crescente
SELECT LNAME FROM USERS ORDER BY LNAME ASC LIMIT 5;

-- Busca com LIKE
-- Seleciona todos os usuários cujo FNAME contém 'IND'
SELECT * FROM USERS WHERE FNAME LIKE '%IND%';
-- Seleciona todos os usuários cujo LNAME tem 'OE' na segunda e terceira posição
SELECT * FROM USERS WHERE LNAME LIKE '_OE';

-- Contagem COUNT
-- Conta o número total de registros na tabela USERS
SELECT COUNT(*) FROM USERS;
-- Conta o número de sobrenomes na tabela USERS
SELECT COUNT(LNAME) FROM USERS;
-- Conta o número de usuários com o primeiro nome 'MICHAEL'
SELECT COUNT(*) FROM USERS WHERE FNAME = 'MICHAEL';
-- Conta o número de usuários com o primeiro nome 'JANE'
SELECT COUNT(*) FROM USERS WHERE FNAME = 'JANE';

-- Funções Agregadas (MIN/MAX/AVG/SUM)
-- Seleciona a idade mínima dos usuários
SELECT MIN(AGE) FROM USERS;
-- Seleciona a idade máxima dos usuários
SELECT MAX(AGE) FROM USERS;
-- Calcula a idade média dos usuários
SELECT AVG(AGE) FROM USERS;
-- Soma as idades dos usuários
SELECT SUM(AGE) FROM USERS;

-- Agrupamento GROUP BY
-- Agrupa os usuários pelo primeiro nome e calcula a idade média
SELECT FNAME, AVG(AGE) AS AVERAGE_AGE FROM USERS GROUP BY FNAME;

-- Condições (!=, =, <, >)
-- Seleciona usuários com idade diferente de 35
SELECT FNAME, LNAME, AGE FROM USERS WHERE AGE != 35;
-- Seleciona usuários com primeiro nome diferente de 'JANE'
SELECT FNAME, LNAME, AGE, PASSW FROM USERS WHERE FNAME != 'JANE';
-- Seleciona usuários com senha diferente de 'Pa$$w0rd123'
SELECT FNAME, AGE FROM USERS WHERE PASSW != 'Pa$$w0rd123';
-- Seleciona usuários com idade maior que 10
SELECT PASSW FROM USERS WHERE AGE > 10;
-- Seleciona usuários com idade menor ou igual a 30
SELECT * FROM USERS WHERE AGE <= 30;
-- Seleciona usuários com comprimento do primeiro nome menor que 10
SELECT * FROM USERS WHERE LENGTH(FNAME) < 10;

-- Operadores AND/OR/BETWEEN/IN
-- Seleciona usuários com primeiro nome 'LINDA' e sobrenome 'WILSON'
SELECT * FROM USERS WHERE FNAME = 'LINDA' AND LNAME = 'WILSON';
-- Seleciona usuários com primeiro nome 'NOTHING' ou 'DAVID' ou sobrenome 'BROWN'
SELECT * FROM USERS WHERE FNAME = 'NOTHING' OR FNAME = 'DAVID' OR LNAME = 'BROWN';
-- Seleciona usuários com idade entre 26 e 30
SELECT * FROM USERS WHERE AGE BETWEEN 26 AND 30;
-- Seleciona usuários com idade em 25, 30, 35 ou 45
/* SELECT * FROM USERS WHERE AGE IN (25, 30, 35, 45); */
-- Seleciona usuários com primeiro nome 'JANE', 'DAVID' ou 'MICHAEL'
/* SELECT * FROM USERS WHERE FNAME IN ('JANE', 'DAVID', 'MICHAEL'); */
-- Seleciona usuários com email específico
SELECT * FROM USERS WHERE EMAIL IN ('david.anderson@example.com', 'jane.smith@example.com');

-- CASE Statement (comentado no código original)
/*
SELECT *, 
CASE 
    WHEN AGE < 20 THEN 'YOUNG'
    WHEN AGE BETWEEN 20 AND 40 THEN 'ADULT'
    ELSE 'OLD'
END AS AGE_GROUP 
FROM USERS;
*/

