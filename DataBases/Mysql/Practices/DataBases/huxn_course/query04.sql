
--DB RELATIONSHIPS  
/*
- OBS: O RELACIONAMENTO ENTRE AS TABELAS QUE ESTÃO DE DENTRO DE UM BANCO DE DADOS SÃO OQ FAZ BANCOS RELACIONAIS SEREM RELACIONAIS
- OBS: NÃO OCORRE RELACIONAMENTO ENTRE BANCO DE DADOS.(ATÉ EXISTE, MAS NÃO SEI SE VC VAI QUERER TENTAR FAZER.)
- (FOREIGN KEY): VINCULO/Relacionamento entre tabelas, restrição, referência, coluna, tabela pai, tabela filho.
*/

-- 00 ONE TO ONE (NÃO USADO!).
--------------------------------

-- 01 ONE TO MANY
-- TEST 01
---------------------------------
CREATE TABLE ENGINEER (
    ENG_ID int AUTO_INCREMENT PRIMARY KEY,
    ENG_NAME VARCHAR(55) NOT NULL,
    PROFI VARCHAR(200) NOT NULL,
    EMAIL VARCHAR(50)
)

CREATE TABLE TASKS (
    TID INT AUTO_INCREMENT PRIMARY KEY,
    TNAME VARCHAR(200),
    TDESCRIPTION TEXT,
    ENG_ID INT,
    FOREIGN KEY (ENG_ID) REFERENCES ENGINEER(ENG_ID)
)

INSERT INTO ENGINEER (ENG_NAME, PROFI, EMAIL) VALUES
    ('ALICE JONH', 'FULL-STACK', 'ALICEJOHN@GMAIL.COM'),
    ('BOB NUEMAN', 'BACK-STACK', 'BOBNUEMAN@GMAIL.COM'),
    ('BOUCHER MABALOUIS','FRONT-END','BOUCHER@GMAIL.COM')

INSERT INTO ENGINEER (ENG_NAME, PROFI, EMAIL) VALUES
    ('CARLENS OSLIN' ,'JUNIOR BACK-END','SPOT-SERVER');

    
INSERT INTO TASKS (TNAME, TDESCRIPTION, ENG_ID) VALUES
    ('TS 1', 'DESIGN FIGMA', 1),
    ('TS 2', 'LOGIC BUILD', 2),
    ('TS 3', 'SERVICE UI', 1),
    ('TS 4', 'WEBSITE IMPRESS', 3),
    ('TS 5', 'PROJECT OPENIA', 1)


SELECT * FROM TASKS;
SELECT * FROM ENGINEER;

-- TEST02
CREATE TABLE autores (
    autor_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE livros (
    livro_id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
);

INSERT INTO autores (nome) VALUES ('Stephen King');
SELECT autor_id FROM autores WHERE nome = 'Stephen King';
INSERT INTO livros (titulo, autor_id) VALUES ('It', 1);

SELECT * FROM AUTORES, LIVROS;



**02 MANY TO MANY**
--TEST01
-----------------------------------------------

-- TEST02
CREATE TABLE produtos (
    produto_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE categorias (
    categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE produtos_categorias (
    produto_id INT,
    categoria_id INT,
    PRIMARY KEY (produto_id, categoria_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

INSERT INTO produtos (nome) VALUES ('Camiseta');

INSERT INTO produtos_categorias (produto_id, categoria_id) VALUES (1, 1); -- Exemplo: Camisetas pertencem à categoria 1 (roupas)
INSERT INTO produtos_categorias (produto_id, categoria_id) VALUES (1, 2); -- Exemplo: Camisetas também podem pertencer à categoria 2 (promoção)

