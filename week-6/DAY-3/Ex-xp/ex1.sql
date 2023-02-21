-- select film.title, film.description, language.name from film
-- join language on film.language_id = language.language_id;

-- create table new_film (
-- id serial primary key, 
-- name varchar(50)
-- );

-- insert into new_film (name) values
-- ('titanic'), ('prison break'), ('divergente');
-- create table customer_review1 (
-- review_id serial not null,
-- film_id int,
-- language_id int,
-- title varchar(100),
-- score int,
-- review_text text, 
-- last_update timestamp,
-- PRIMARY KEY (review_id),
--         CONSTRAINT fk_film_id
--         FOREIGN KEY (film_id)
--             REFERENCES new_film (id)
--             ON DELETE CASCADE,
--         FOREIGN KEY (language_id)
--             REFERENCES language (language_id)
-- 	);
-- on delete cascade = quand je supprime un truc le tableau retrecis

--  insert into customer_review1 (film_id, language_id, title, score, review_text, last_update)
--  values(7, 1, 'titanic', 9, 'very good moovie', '15/08/2002'),
--  (9, 2, 'divergente', 4, 'my favorite moovie', '24/08/2002');

-- delete from new_film where id = 7;
