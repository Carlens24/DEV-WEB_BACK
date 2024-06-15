SELECT FNAME FROM USERS
WHERE `FNAME` IN ('Linda', 'William', 'Sarah', 'John');

-- CASE STATMENT
SELECT 
    FNAME,     -- Supondo que exista uma coluna USER_ID na tabela USERS
    AGE,
    CASE
        WHEN AGE BETWEEN 20 AND 29 THEN 'YOUNG'
        WHEN AGE BETWEEN 30 AND 60 THEN 'MIDDLE-AGED'
        ELSE 'OLD SENIOR!!'
    END AS AGE_GROUP
FROM USERS;

-- UNIQUE/CHECK
CREATE TABLE SERIES (
    ID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    TITLE VARCHAR(255) UNIQUE,
    RELEASE_YEAR INT,
    GENRE VARCHAR(255),
    CONSTRAINT chk_release_year CHECK (RELEASE_YEAR >= 2020),
    CONSTRAINT chk_genre CHECK (GENRE = 'ACTION' OR GENRE = 'DRAMA')
);


INSERT INTO SERIES (ID, TITLE, RELEASE_YEAR, GENRE) VALUES
(DEFAULT, 'The Queens Gambit', 2020, 'DRAMA'),
(DEFAULT, 'Bridgerton', 2020, 'DRAMA'),
(DEFAULT, 'The Mandalorian', 2020, 'ACTION'),
(DEFAULT, 'The Boys', 2020, 'ACTION'),
(DEFAULT, 'Shadow and Bone', 2021, 'DRAMA');

SELECT * FROM SERIES;

INSERT INTO SERIES (ID, TITLE, RELEASE_YEAR, GENRE) VALUES
    (DEFAULT, 'Breaking Bad', 2008, 'Crime, Drama, Thriller'),
    (DEFAULT, 'Game of Thrones', 2011, 'Action, Adventure, Drama'),
    (DEFAULT, 'Stranger Things', 2016, 'Drama, Fantasy, Horror'),
    (DEFAULT, 'The Crown', 2016, 'Biography, Drama, History'),
    (DEFAULT, 'The Mandalorian', 2019, 'Action, Adventure, Fantasy'),
    (DEFAULT, 'Sherlock', 2010, 'Crime, Drama, Mystery'),
    (DEFAULT, 'Friends', 1994, 'Comedy, Romance'),
    (DEFAULT, 'The Office', 2005, 'Comedy'),
    (DEFAULT, 'Black Mirror', 2011, 'Drama, Sci-Fi, Thriller'),
    (DEFAULT, 'The Witcher', 2019, 'Action, Adventure, Drama');

-- ALTER TABLE
ALTER TABLE SERIES
DROP COLUMN RELEASE_YEAR;

ALTER TABLE SERIES
MODIFY COLUMN TITLE VARCHAR(500);

ALTER TABLE SERIES
ADD COLUMN TEST_CLMN VARCHAR(50);

INSERT INTO SERIES (TEST_CLMN) VALUES
('TESTANDO!!!')
