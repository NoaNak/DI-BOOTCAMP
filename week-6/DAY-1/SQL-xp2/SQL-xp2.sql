-- create table students(
-- id serial primary key, last_name varchar, first_name varchar, birth_date date);
-- insert into students values 
-- (Default,'Benichou','Marc','1998-11-02'),
-- (Default,'Cohen','Yann','2010-12-03'),
-- (Default,'Benichou','Lea','1987-07-27'),
-- (Default,'Dux','Amelia','1996-04-07'),
-- (Default,'Grez','David','2003-06-14'),
-- (Default,'Simpson','Omer','1980-10-03');

-- insert into students
-- values
-- (Default,'Nakache','Noa','2002-08-24');

-- select * from students;
-- select last_name, first_name from students;
-- select last_name, first_name from students where id=2;
-- select last_name, first_name from students where last_name='Marc' and first_name='Benichou';
-- select last_name, first_name from students where last_name='Benichou' or first_name='Marc';
-- select last_name, first_name from students where last_name like '%a%';
-- select last_name, first_name from students where last_name like 'a%';
-- -- %a% = mot qui contiennent la lettre a
-- -- a% = mot qui commence par la lettre a 
-- select last_name, first_name from students where last_name like '%a';
-- select last_name, first_name from students where last_name='%a_';
-- -- %a_ = on prend l'avant derniere lettre 
-- select last_name, first_name from students where id=1 and id=3;
-- select last_name, first_name from students where birth_date > '2002-01-01';



