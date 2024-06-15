-- **DATABASE CREATION**
CREATE DATABASE HuXn_course;

-- SHOW DATABASES;
-- USE HuXn_course;

-- TABLE COLUNMS CREATION
CREATE TABLE GAMES(
    ID INT PRIMARY KEY AUTO_INCREMENT UNIQUE,  -- ID único e auto-incremento
    NAME VARCHAR(50),  -- Nome do jogo
    RELEASE_YEAR INT DEFAULT 2025,  -- Ano de lançamento, padrão 2025
    RATINGS INT NOT NULL,  -- Avaliação do jogo (não nulo)
    INFOS TEXT  -- Informações adicionais
);

-- TABLE COLUNMS CREATION
CREATE TABLE MOVIES(
    ID INT PRIMARY KEY AUTO_INCREMENT UNIQUE,  -- ID único e auto-incremento
    TITLE VARCHAR(50),  -- Título do filme
    RELEASE_YEAR INT,  -- Ano de lançamento
    RATING DECIMAL(3, 1),  -- Avaliação do filme com um decimal
    COMMENT CHAR(50),  -- Comentário sobre o filme
    COMMENT_DATE DATE DEFAULT "2025-04-02",  -- Data do comentário, padrão 2025-04-02
    COMMENT_TIME TIME DEFAULT "14:10:23"  -- Hora do comentário, padrão 14:10:23
);

-- INSERTING DATAS
INSERT INTO GAMES(ID, NAME, RELEASE_YEAR, RATINGS) VALUES
    (DEFAULT, 'GTA 6', 2020, 6),
    (DEFAULT, 'GTA 5', 2010, 10),
    (DEFAULT, 'GTA 4', 2019, 9),
    (DEFAULT, 'BATMAN KNIGHT', 2018, 8),
    (DEFAULT, 'FIFA 2025', 2019, 9),
    (DEFAULT, 'MINECRAFT', 2016, 7),
    (DEFAULT, 'CYBERPUNK 2077', 2020, 7),
    (DEFAULT, 'THE WITCHER 3', 2015, 10),
    (DEFAULT, 'RED DEAD REDEMPTION 2', 2018, 10),
    (DEFAULT, 'OVERWATCH', 2016, 9),
    (DEFAULT, 'FORTNITE', 2017, 8),
    (DEFAULT, 'DOOM ETERNAL', 2020, 8),
    (DEFAULT, 'HALO INFINITE', 2021, 7),
    (DEFAULT, 'THE LEGEND OF ZELDA: BREATH OF THE WILD', 2017, 10),
    (DEFAULT, 'GOD OF WAR', 2018, 10),
    (DEFAULT, 'CALL OF DUTY: MODERN WARFARE', 2019, 8),
    (DEFAULT, 'ASSASSIN\'S CREED VALHALLA', 2020, 8),
    (DEFAULT, 'ANIMAL CROSSING: NEW HORIZONS', 2020, 9),
    (DEFAULT, 'SEKIRO: SHADOWS DIE TWICE', 2019, 9),
    (DEFAULT, 'FINAL FANTASY VII REMAKE', 2020, 9),
    (DEFAULT, 'DESTINY 2', 2017, 8);

-- INSERTING DATAS
INSERT INTO MOVIES(ID, TITLE, RELEASE_YEAR, RATING, COMMENT) VALUES
    (DEFAULT, 'Inception', 2010, 8.8, 'Excellent'),
    (DEFAULT, 'The Godfather', 1972, 9.2, 'Classic'),
    (DEFAULT, 'Pulp Fiction', 1994, 8.9, 'Iconic'),
    (DEFAULT, 'The Dark Knight', 2008, 9.0, 'Epic'),
    (DEFAULT, 'Forrest Gump', 1994, 8.8, 'Heartfelt'),
    (DEFAULT, 'The Matrix', 1999, 8.7, 'Mind-blow'),
    (DEFAULT, 'Fight Club', 1999, 8.8, 'Cult'),
    (DEFAULT, 'Interstellar', 2014, 8.6, 'Stunning'),
    (DEFAULT, 'The Shawshank Redemption', 1994, 9.3, 'Good'),
    (DEFAULT, 'The Lion King', 1994, 8.5, 'Classic'),
    (DEFAULT, 'Gladiator', 2000, 8.5, 'Epic'),
    (DEFAULT, 'Titanic', 1997, 7.8, 'Romantic'),
    (DEFAULT, 'Avatar', 2009, 7.8, 'Visuals'),
    (DEFAULT, 'Jurassic Park', 1993, 8.1, 'Adventure'),
    (DEFAULT, 'The Avengers', 2012, 8.0, 'Superhero'),
    (DEFAULT, 'Toy Story', 1995, 8.3, 'Animated'),
    (DEFAULT, 'Braveheart', 1995, 8.3, 'Historical'),
    (DEFAULT, 'Casablanca', 1942, 8.5, 'Romantic'),
    (DEFAULT, 'The Wizard of Oz', 1939, 8.0, 'Magical'),
    (DEFAULT, 'Gone with the Wind', 1939, 8.1, 'Epic');



-- SELECT
-- SELECTING ALL FROM MOVIES
SELECT * FROM MOVIES;


-- SELECTING SPECIFIC DATAS
SELECT COMMENT, RELEASE_YEAR FROM MOVIES;

-- SELECTING ALL FROM GAMES
SELECT * FROM GAMES;

-- SELECTING SPECIFIC DATAS
SELECT RELEASE_YEAR FROM GAMES;


-- SELECTING WHERE DATAS ARE
SELECT * FROM MOVIES WHERE COMMENT = 'EPIC';
SELECT TITLE FROM MOVIES WHERE COMMENT = 'CLASSIC';
SELECT TITLE, RATING FROM MOVIES WHERE COMMENT = 'Mind-blow';
SELECT TITLE, RELEASE_YEAR FROM MOVIES WHERE RATING = '8.0';


-- RENAME
SELECT ID AS ID_MOVIES FROM MOVIES;
SELECT TITLE AS MOVIE_NAME FROM MOVIES;
SELECT RATING AS MOVIE_RATING FROM MOVIES;

-- UPDATING DATAS
UPDATE MOVIES
SET COMMENT = 'CLASSIC'
WHERE COMMENT = 'GOOD';

SELECT * FROM MOVIES;

-- DELETING TABLES
-- DROP TABLE GAMES, MOVIES;



USE CADASTRO;
SELECT * FROM GAFANHOTOS;
UPDATE GAFANHOTOS
SET NOME = 'OSLIN'
WHERE ID = '1';
SELECT * FROM GAFANHOTOS;
UPDATE GAFANHOTOS
SET PROF = 'ARTE'
WHERE ID = '1';
UPDATE GAFANHOTOS
SET PROF = 'TESTE...';
DELETE FROM CURSOS
WHERE IDCURSOS = '5';
SELECT * FROM CURSOS;
DELETE FROM CURSOS;


-- TYPE OF DATAS ---------------------------------------------------------------------------------------
/*
1. Numeric Types:
   - INT or INTEGER: Integer numbers.
   - TINYINT: Very small integer numbers.
   - SMALLINT: Small integer numbers.
   - MEDIUMINT: Medium-sized integer numbers.
   - BIGINT: Large integer numbers.
   - FLOAT: Single-precision floating-point numbers.
   - DOUBLE or REAL: Double-precision floating-point numbers.
   - DECIMAL or NUMERIC: Fixed-point decimal numbers.

2. Date and Time Types:
   - DATE: Date in 'YYYY-MM-DD' format.
   - TIME: Time in 'HH:MM:SS' format.
   - DATETIME: Date and time in 'YYYY-MM-DD HH:MM:SS' format.
   - TIMESTAMP: Date and time record, often used to track changes in rows.
   - YEAR: Four-digit year format (e.g., 'YYYY').

3. String Types:
   - CHAR: Fixed-length string.
   - VARCHAR: Variable-length string.
   - TEXT: Long string.
   - BINARY: Fixed-length binary string.
   - VARBINARY: Variable-length binary string.
   - BLOB: Long binary data.

4. Miscellaneous Types:
   - ENUM: List of allowed values.
   - SET: Set of allowed values.
   - BOOL, BOOLEAN: Boolean type, usually stored as 0 (false) or 1 (true).

5. Spatial Types:
   - GEOMETRY, POINT, LINESTRING, POLYGON, etc.: Data types for storing spatial data (GIS).
*/

-- MORE EXEMPLES ---------------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS COMMENTS (
    ID INT AUTO_INCREMENT PRIMARY KEY,  -- ID único e auto-incremento
    AUTHOR VARCHAR(159),  -- Autor do comentário
    CONTENT VARCHAR(159),  -- Conteúdo do comentário
    CREATE_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Data e hora da criação, padrão é o momento atual
    UPDATE_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Data e hora da atualização, atualizado automaticamente
);

SELECT * FROM COMMENTS;

INSERT INTO COMMENTS (AUTHOR, CONTENT) VALUES
    ('Alice', 'This is a great article!'),
    ('Bob', 'I totally agree with this point of view.'),
    ('Charlie', 'Could you provide more details on this topic?'),
    ('Diana', 'This is very helpful, thanks for sharing!'),
    ('Eve', 'I have a different perspective on this matter.'),
    ('Frank', 'Excellent write-up, keep it up!'),
    ('Grace', 'This article is very informative.'),
    ('Heidi', 'I found this very interesting and enlightening.'),
    ('Ivan', 'Great insights, thank you!'),
    ('Judy', 'Can you explain the last point further?');

UPDATE COMMENTS 
SET CONTENT = 'WFT ARE YOU TRYING TO SAY HERE?'
WHERE ID = '3';