CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

-- SERIAL (1, 2, 3, 4...)
-- PRIMARY KEY - IDENTIFIER, UNIQUE (like passport number) 

-- Contraint
-- NOT NULL - don't accept NULL values

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt', 'Damon', '08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George', 'Clooney', '06/05/1961', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('John', 'Krasinsky', '1960-09-10', 2),
('Juan', 'Perez', '1978-10-10', 6),
('Ana', 'Rodriguez', '1995-03-08', 10);

-- Add two more female actors in the table actors. Add them one by one
-- Add three more actors, add all of them in one query !
-- Retrieve everything from the table actors




-- Daily
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?


-- select count(*) from actors;

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES(null, 'Damon', '08/10/1970', 5);