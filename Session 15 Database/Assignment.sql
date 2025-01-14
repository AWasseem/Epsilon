use employees;
-- Github URL 
-- 1 - Select all data from the “departments” table.
SELECT 
    *
FROM
    departments;


-- 2 - Select the “dept_no” column of the “departments”
select dept_no
from
departments;


-- 3 - Select all people from the “employees” table whose first name is “Elvis”.
select *
from 
employees
where
first_name like 'Elvis';


-- 4 - Select all female employees whose first name is Kellie. 
select *
from 
employees
where
first_name = 'Kellie'
and
gender ='F';

-- 5 - Select all employees whose first name is either Kellie or Aruna.
select *
from 
employees
where
first_name ='Kellie' or first_name='Aruna';



-- 6 - Select all female whose first name is either Kellie or Aruna.
select *
from 
employees
where
(first_name ='Kellie' or first_name='Aruna')
and
gender ='F';


-- 7 - Use the IN operator to select all individuals from the “employees” table, whose first name is either “Denis”, or “Elvis”.
select *
from 
employees
where
first_name in ('Denis','Elvis');

-- 8 - Extract all records from the ‘employees’ table, aside from those with employees named John, Mark, or Jacob.
select *
from 
employees
where
first_name not in ('John','Mark','Jacob');

-- 9 - Working with the “employees” table, use the LIKE operator to select the data about all individuals, whose first name starts with “Mark”; specify that the name can be succeeded by any sequence of characters.
select *
from 
employees
where
first_name like 'Mark%';

-- 10 - Retrieve a list with all employees who have been hired in the year 2000.
select *
from 
employees
where
year(hire_date)=2000;

-- 11 - Retrieve a list with all employees whose employee number is written with 5 characters, and starts with “1000”. 
select *
from 
employees
where
emp_no like '1000_';

-- 12 - Extract all individuals from the ‘employees’ table whose first name contains “Jack”.
select *
from 
employees
where
first_name like '%jack%';

-- 13 - Once you have done that, extract another list containing the names of employees that do not contain “Jack”.
select *
from 
employees
where
first_name not like '%jack%';

 
-- 14 - Select all the information from the “salaries” table regarding contracts from 66,000 to 70,000 dollars per year.
select *
from
salaries
where
salary between 66000 and 70000 ;


-- 15 - Retrieve a list with all individuals whose employee number is not between ‘10004’ and ‘10012’.
select *
from 
employees
where
emp_no not between 10004 and 10012;

-- 16 - Select the names of all departments with numbers between ‘d003’ and ‘d006’. 
select dept_no,dept_name
from
departments
where
dept_no between 'd003' and 'd006';

-- 17 - Select the names of all departments whose department number value is not null.
select dept_name
from
departments
where
dept_no is not null;

-- 18 - Retrieve a list with data about all female employees who were hired in the year 2000 or after.
select *
from
employees
where
gender ='F'
and
year(hire_date) >= 2000;

-- 19 - Extract a list with all employees’ salaries higher than $150,000 per annum.
select emp.emp_no,emp.first_name,emp.last_name,sal.salary
from
employees as emp
inner join
salaries as sal on emp.emp_no = sal.emp_no
where
sal.salary >150000;
