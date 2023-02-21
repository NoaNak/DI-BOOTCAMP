CREATE TABLE scenarios (
  pk_movie_id int primary key,
  scenario_story text not null,
  constraint pk_movie_id foreign key (pk_movie_id) references movies(movie_id)
);

-- constraint - a rule 
-- EXAMPLES
-- pk_movie_id IS PRIMARY KEY
-- to create a constraint
-- 			constraint [name of constraint(pk_movie_id)] [rule name (foreign key)] references movies(movie_id)

insert into scenarios (pk_movie_id, scenario_story)
values
((select movie_id from movies where title = 'The quiet place'), 'Horror movie where everybody are quit.');