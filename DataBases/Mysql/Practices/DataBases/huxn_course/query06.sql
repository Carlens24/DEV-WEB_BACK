-- Creating the FILMES table
CREATE TABLE FILMES (
    FILM_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    TITLE VARCHAR(50) NOT NULL,
    YEAR INT NOT NULL,
    DIRECTOR VARCHAR(50) NOT NULL,
    GENRE VARCHAR(50) NOT NULL 
);

-- Creating the PERSON table
CREATE TABLE PERSON (
    PERSON_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(60),
    AGE INT,
    EMAIL VARCHAR(50),
    GENDER VARCHAR(50),
    COUNTRY VARCHAR(50)
);

-- Creating the COMMENT table
CREATE TABLE COMMENT (
    COMMENT_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    CONTENT TEXT NOT NULL,
    FILM_ID INT NOT NULL,
    PERSON_ID INT NOT NULL,
    FOREIGN KEY (FILM_ID) REFERENCES FILMES (FILM_ID),
    FOREIGN KEY (PERSON_ID) REFERENCES PERSON (PERSON_ID)
);

-- Inserting data into the FILMES table
INSERT INTO FILMES (TITLE, YEAR, DIRECTOR, GENRE) VALUES
('Inception', 2010, 'Christopher Nolan', 'Sci-Fi'),
('The Matrix', 1999, 'Lana Wachowski, Lilly Wachowski', 'Action'),
('Interstellar', 2014, 'Christopher Nolan', 'Sci-Fi'),
('The Godfather', 1972, 'Francis Ford Coppola', 'Crime'),
('Pulp Fiction', 1994, 'Quentin Tarantino', 'Crime'),
('The Dark Knight', 2008, 'Christopher Nolan', 'Action'),
('Fight Club', 1999, 'David Fincher', 'Drama'),
('Forrest Gump', 1994, 'Robert Zemeckis', 'Drama'),
('The Shawshank Redemption', 1994, 'Frank Darabont', 'Drama'),
('The Lord of the Rings: The Fellowship of the Ring', 2001, 'Peter Jackson', 'Fantasy');

-- Inserting data into the PERSON table
INSERT INTO PERSON (NAME, AGE, EMAIL, GENDER, COUNTRY) VALUES
('John Doe', 30, 'johndoe@example.com', 'Male', 'USA'),
('Jane Smith', 28, 'janesmith@example.com', 'Female', 'UK'),
('Michael Johnson', 35, 'michaelj@example.com', 'Male', 'Canada'),
('Emily Davis', 22, 'emilyd@example.com', 'Female', 'Australia'),
('Robert Brown', 40, 'robertb@example.com', 'Male', 'USA'),
('Linda Williams', 33, 'lindaw@example.com', 'Female', 'USA'),
('James Miller', 45, 'jamesm@example.com', 'Male', 'UK'),
('Patricia Taylor', 27, 'patriciat@example.com', 'Female', 'Canada'),
('David Anderson', 38, 'davida@example.com', 'Male', 'Australia'),
('Sarah Thomas', 31, 'saraht@example.com', 'Female', 'USA');

-- Inserting data into the COMMENT table
INSERT INTO COMMENT (FILM_ID, PERSON_ID, CONTENT) VALUES
(1, 1, 'Amazing movie with a mind-bending plot!'),
(2, 2, 'A groundbreaking film in the action genre.'),
(3, 3, 'A visually stunning masterpiece.'),
(4, 4, 'An all-time classic with outstanding performances.'),
(5, 5, 'A unique blend of dark humor and crime.'),
(6, 6, 'An epic and thrilling superhero movie.'),
(7, 7, 'A thought-provoking drama with a cult following.'),
(8, 8, 'A heartwarming story with memorable characters.'),
(9, 9, 'An inspiring tale of hope and friendship.'),
(10, 10, 'A magical adventure that set the standard for fantasy films.');


SELECT * FROM FILMES F
RIGHT JOIN PERSON P ON F.FILM_ID = P.PERSON_ID; 