-- create table Customer1(
-- 	id serial primary key,
-- 	first_name varchar(100) not null,
-- 	last_name varchar(100) not null
-- );

-- create table Customer_Profile(
-- 	id serial primary key,
-- 	isLoggedIn boolean default false,
-- 	customer_id INTEGER REFERENCES Customer(id),
-- primary key (customer_id)
-- );

-- insert into Customer1 (first_name, last_name) values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- insert into Customer_Profile(isLoggedIn, customer_id) values
-- (true,( select  id from Customer1 
-- where first_name = 'John')),
-- (false, (select false, id from Customer1
-- where first_name = 'Jerome'));

-- SELECT Customer.first_name 
-- FROM Customer
-- JOIN Customer_Profile ON Customer.id = Customer_Profile.customer_id
-- WHERE Customer_Profile.isLoggedIn = true;

-- select count(*)
-- from customer as c
-- inner join customer_profile as cp
-- on c.id = cp.customer_id
-- where cp.isLoggedIn = false;

-- create table book (
-- book_id serial primary key,
-- title varchar(30) not null,
-- author varchar(30) not null
-- );

-- insert into book (title, author) values
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student(
-- student_id serial primary key,
-- name varchar(30) NOT NULL UNIQUE,
-- age int check (age <= 15)
-- )

-- insert into Student (name, age) values
--   ('John', 12),
--   ('Lera', 11),
--   ('Patrick', 10),
--   ('Bob', 14);

-- create table library(
-- 	book_fk_id int references Book(book_id) on delete cascade on update cascade,
-- -- 	quand il y a int alors j ajoute references (je fais une relationship)
-- 	-- 	si je fais delete - ca supp juste linfo, mais delete cascade - supp toute les infos de la column
-- 	student_fk_id int references Student(student_id) on delete cascade on update cascade,
-- 	borrowed_date date
-- );


-- insert into library (book_fk_id, student_fk_id, borrowed_date)
--   values 
-- 	((select book_id from Book where title = 'Alice In Wonderland'),
-- 	(select student_id from Student where name = 'John'),'2022-02-15'),

-- 	   ((select book_id from Book where title = 'To kill a mockingbird'),
--     (select student_id from Student where name = 'Bob'),
--     '2021-03-03'),
  
--     ((select book_id from Book where title = 'Alice In Wonderland'),
--     (SELECT student_id from Student where name = 'Lera'),
--     '2021-05-23'),
  
-- 	   ((select book_id from Book where title = 'Harry Potter'),
--     (select student_id from Student where name = 'Bob'),
--     '2021-08-12');

-- select * from Library;

-- select Student.name, Book.title
-- from Library
-- join Student on Library.student_fk_id = Student.student_id
-- join Book on Library.book_fk_id = Book.book_id;

-- select avg (student.age) from library
-- join Student on Library.student_fk_id = Student.student_id
-- join Book on Library.book_fk_id = Book.book_id
-- where Book.title = 'Alice In Wonderland';

-- delete from student where name = 'John';
-- delete from student where name = 'Bob';


  


