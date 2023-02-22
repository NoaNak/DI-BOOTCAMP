-- select first_name as first, last_name as last from employees;

-- select distinct department_id from employees;

-- select * from employees 
-- order by first_name desc;

-- select first_name, last_name, salary, (salary * 0.15) as PF from employees;

-- select employee_id, first_name, last_name, salary 
-- from employees
-- order by salary asc;

-- select sum(salary) as total_salary from employees;

-- select max(salary), min(salary) from employees;

-- select avg(salary) from employees;

-- select count(*) from employees;

-- select upper (first_name) from employees;

-- select substring(first_name, 1, 3) from employees;
-- pour recup les trois prem charac de chaque prenom

-- select first_name|| ' ' ||last_name as full_name from employees;
-- cest pour que le first et last soit reuni en un full name 

-- select first_name, last_name, length(CONCAT(first_name, ' ', last_name)) from employees;

-- select * from employees where  REGEXP_LIKE(first_name, '[0-9]')
-- REGEXP_LIKE est une fonction SQL utilisée pour rechercher un modèle d'expression régulière dans une chaîne. Elle renvoie une valeur booléenne (vrai ou faux) selon que le motif se trouve ou non dans la chaîne.

-- select * from countries
-- limit 10;


-- PART 2
-- select first_name, last_name, salary from employees
-- where salary between 10.000 and 15.000;

-- select first_name, last_name, hire_date from employees
-- where hire_date between '1987-01-01' and '1987-12-31';

-- select * from employees
-- where first_name like '%c%e%';

-- select last_name, job_id, salary from employees
-- where job_id not in ('9','17')
-- and salary not in (4500, 10000, 15000);

-- select last_name from employees
-- where length(last_name) = 6;

-- select last_name from employees
-- where last_name like '__e%';

-- select distinct job_id
-- from employees;

-- select * from employees 
-- where last_name in ('Jones', 'Blake', 'Scott', 'King', 'Ford');
