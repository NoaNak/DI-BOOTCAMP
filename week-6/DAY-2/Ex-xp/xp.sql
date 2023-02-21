-- 1- In the dvdrental database write a query to select all the columns from the “customer” table.
select * from customer

-- 2- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
select first_name || ' ' || last_name
as full_name from customer;

-- 3- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
select distinct create_date from customer

-- 4- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
select * from customer
order by first_name desc;

-- 5- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
select film_id, title, description, release_year, rental_rate from film
order by rental_rate ASC

-- 6- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
select first_name, last_name, district from customer
inner join address on customer.address_id = address.address_id 
where district = 'Texas'
-- inner join = rejoindre entre eux 

-- 7- Write a query to retrieve all movie details where the movie id is either 15 or 150.
select * from film 
where film_id = 15 or film_id = 150

-- 8- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
select film_id, title, description, length, rental_rate from film
where title = 'prison break';

-- 9- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
select film_id, description, length, rental_rate from film 
where title ilike 'pr%'

-- 10- Write a query which will find the 10 cheapest movies.
select * from film
order by rental_rate asc 
limit 10;

-- 11- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
select * from film
order by rental_rate asc offset 10 fetch first 10 row only
-- offset = pour que ca conserve les 10 d'avant et que ca selectionne les 10 prochains

-- 12- Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select customer.customer_id, customer.first_name, customer.last_name, payment.payment_date, payment.amount from customer 
inner join payment on payment.customer_id = customer.customer_id 
order by customer.customer_id

13- 

14- Write a query to find which city is in which country.

