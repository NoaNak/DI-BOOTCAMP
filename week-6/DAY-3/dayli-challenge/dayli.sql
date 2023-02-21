-- create table Customer1(
-- 	id serial primary key,
-- 	first_name varchar(100) not null,
-- 	last_name varchar(100) not null
-- );

-- create table Customer_Profile(
-- 	id serial primary key,
-- 	isLoggedIn boolean default false,
-- 	customer_id INTEGER REFERENCES Customer(id)
-- );

-- insert into Customer1 (first_name, last_name) values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');



JE COMPREND PAS C CHAT:
-- insert into Customer_Profile(isLoggedIn, customer_id) values
-- (select true, id from Customer1 
-- where first_name = 'John'),
-- (select false, id from Customer1
-- where first_name = 'Jerome');

-- SELECT Customer.first_name 
-- FROM Customer
-- JOIN Customer_Profile ON Customer.id = Customer_Profile.customer_id
-- WHERE Customer_Profile.isLoggedIn = true;

-- SELECT Customer.first_name, COALESCE(Customer_Profile.isLoggedIn, false) AS isLoggedIn
-- FROM Customer
-- LEFT JOIN Customer_Profile ON Customer.id = Customer_Profile.customer_id;


