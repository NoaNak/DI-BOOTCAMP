-- update film 
-- set language_id = '2'
-- where film_id < 10;

-- customer_id and stor_id

--  3- fait

-- select * from rental
-- where return_date is null 

-- select * from film 
-- order by rental_rate desc
-- limit 30;

-- select film.title 
-- from (actor join film_actor on actor.actor_id = film_actor.actor_id)
-- join film on film.film_id = film_actor.film_id
-- where film.description like '%Sumo%' and actor.first_name = 'Penelope' and actor.last_name = 'Monroe';

-- select title from film
-- join film_category on film.film_id = film_category.film_id
-- where category_id = 6 and length < 60 and rating = 'R';


-- RIEN COMPRIS A CA DEMANDER A YOSSI 
-- SELECT film.title, film.description, film.replacement_cost
-- FROM film
-- JOIN inventory
-- ON film.film_id = inventory.film_id
-- JOIN rental
-- ON rental.inventory_id = inventory.inventory_id
-- JOIN customer
-- ON rental.customer_id = customer.customer_id
-- where customer.first_name = 'Matthew'
-- and customer.last_name = 'Mahan'
-- and film.title like '%Boat%' 
-- or film.description like '%Boat%'
-- order by film.replacement_cost desc
-- limit 1 
