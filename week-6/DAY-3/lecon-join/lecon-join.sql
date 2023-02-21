-- get the movie title, actor last name 

select movies.title, actors.last_name 
from actors 
left join movies 
on movies.actor = actors.actor_id;

-- left join gives all rows from the left table(actors) + connected values from the right table(movies)
-- right join - opposite of left join
-- full join - gives all rows from both left and right table