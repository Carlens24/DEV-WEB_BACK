-- VIEWS
CREATE TABLE ANIMES(
ID INT UNIQUE PRIMARY KEY AUTO_INCREMENT, 
NAMES VARCHAR(50),
GENRE TEXT,
START_YEAR YEAR
);

INSERT INTO ANIMES(NAMES, START_YEAR, GENRE) VALUES
('Attack on Titan', 2013, 'Action, Drama'),
('Death Note', 2006, 'Mystery, Psychological, Thriller'),
('Naruto', 2002, 'Action, Adventure, Martial Arts'),
('One Piece', 1999, 'Action, Adventure, Comedy'),
('Dragon Ball Z', 1989, 'Action, Adventure, Martial Arts'),
('Fullmetal Alchemist: Brotherhood', 2009, 'Action, Adventure, Fantasy'),
('My Hero Academia', 2016, 'Action, Adventure, Superhero'),
('Sword Art Online', 2012, 'Action, Adventure, Fantasy'),
('Hunter x Hunter', 2011, 'Action, Adventure, Fantasy'),
('Demon Slayer: Kimetsu no Yaiba', 2019, 'Action, Adventure, Supernatural');

SELECT * FROM ANIMES;

CREATE VIEW ANIMES_NAMES AS 
SELECT ID, CONCAT(NAMES, ' ', GENRE, ' ',START_YEAR) AS FULLCONTENT FROM ANIMES;


SELECT * FROM ANIMES_NAMES;

-- UPDATING VIEW
CREATE OR REPLACE VIEW ANIMES_NAMES AS
SELECT ID, CONCAT(NAMES, ' ', GENRE) AS FULLCONTENT FROM ANIMES
WHERE START_YEAR = 2009;

SELECT * FROM ANIMES_NAMES;

-- DELETING VIEW
DROP VIEW ANIMES_NAMES;