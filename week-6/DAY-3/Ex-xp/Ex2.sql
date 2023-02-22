-- update film 
-- set language_id = '2'
-- where film_id < 10;

-- address_id and stor_id

--  3- fait

-- select * from rental
-- where return_date is null 

-- select inventory_id from rental 
-- where return_date is null;
-- select * from film where film_id in (select film_id 
-- from inventoryjoin rental
-- on rental.inventory_id = inventory.inventory_id
-- where rental.return_date is null)
-- order by rental_rate desc
-- limit 30;

-- select film.title, first_name, last_name
-- from (actor join film_actor on actor.actor_id = film_actor.actor_id)
-- join film on film.film_id = film_actor.film_id
-- where film.description like '%Sumo%' and actor.first_name = 'Penelope' and actor.last_name = 'Monroe';

-- select title from film
-- join film_category on film.film_id = film_category.film_id
-- where category_id = 6 and length < 60 and rating = 'R';


