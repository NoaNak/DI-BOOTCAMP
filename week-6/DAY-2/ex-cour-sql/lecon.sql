select distinct(number_oscars) from actors;
-- returns only the unique values in a column
-- like a set in Python

select * from actors order by age; 
-- desc - descending
-- asc - ascending

-- 'Matt','Lea','Davis'

select * from actors where first_name not in ('Matt','Ana','Davis');


-- between

select * from actors where age not between '1970-01-01' and '1990-01-01';

select * from actors where age > '1970-01-01' and age < '1990-01-01';