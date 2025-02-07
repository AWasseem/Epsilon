use employees;
-- 1- How many annual contracts with a value higher than or equal to $100,000 have been registered in the salaries table?
select count(*) as annual_contracts_count
from 
salaries
where 
salary >= 100000;

-- 2- How many managers do we have in the “employees” database?
select count(*) as count_of_manager from dept_manager;

-- 3-Select all data from the “employees” table, ordering it by “hire date” in descending order.
select *
from
employees
order by hire_date desc;

-- 4- Write a query that obtains two columns. The first column must contain annual salaries higher than 80,000 dollars.
-- The second column, renamed to “emps_with_same_salary”, 
-- must show the number of employees contracted to that salary. Lastly, sort the output by the first column.
select salary,count(salary) as emps_with_same_salary
from
salaries
where
salary > 80000
group by salary
order by salary;

-- 5-Select all employees whose average salary is higher than $120,000 per annum
-- Hint: You should obtain 101 records.
select distinct emp.emp_no,emp.first_name,emp.last_name,sum(sal.salary)/count(emp.emp_no) as average_salary
from
employees as emp
inner join
salaries as sal on emp.emp_no =sal.emp_no
group by emp.emp_no,emp.first_name,emp.last_name
having
sum(sal.salary)/count(emp.emp_no) >120000;

-- 6- Select the employee numbers of all individuals who have signed more than 1 contract after the 1st of January 2000.
-- Hint: To solve this exercise, use the “dept_emp” table.
select emp.emp_no,emp.first_name,count(demp.emp_no) as contract_numbers
from 
employees as emp
inner join
dept_emp as demp on emp.emp_no = demp.emp_no
where
demp.from_date > '2000-1-1' 
group by emp.emp_no,emp.first_name
having count(demp.emp_no) > 1;

-- 7- Select the first 100 rows from the ‘dept_emp’ table. 
select *
from
dept_emp
limit 100;

-- 8-How many departments are there in the “employees” database? Use the ‘dept_emp’ table to answer the question.
select count(distinct dept_emp.dept_no) as count_departments
from
dept_emp ;

-- 9- What is the total amount of money spent on salaries for all contracts starting after the 1st of January 1997?
select sum(salary) as total_amount_of_money_spent
from
salaries
where
 from_date >'1997-1-1';
 
 -- 10- Which is the lowest employee number in the database?
 select min(emp_no)
 from
 employees;

-- 11-What is the average annual salary paid to employees who started after the 1st of January 1997?
select distinct emp.emp_no,emp.first_name,emp.last_name,sum(sal.salary)/count(emp.emp_no) as average_salary
from
employees as emp
inner join
salaries as sal on emp.emp_no =sal.emp_no
where
emp.hire_date > '1997-1-1'
group by emp.emp_no,emp.first_name,emp.last_name;

-- 12- Extract the information about all department managers who were hired between the 1st of January 1990 and the 1st of January 1995.
select emp.*,dept.*
from
employees as emp
inner join
dept_manager as dm on emp.emp_no = dm.emp_no
inner join
departments dept on dept.dept_no = dm.dept_no
where
emp.hire_date between '1990-1-1' and '1995-1-1';

-- 13- Get the employee numbers who are in Human Resource department
select emp.*,dept.*
from
employees as emp
inner join
dept_emp as dm on emp.emp_no = dm.emp_no
inner join
departments dept on dept.dept_no = dm.dept_no
where
dept.dept_name='Human Resources';

-- 14 - get the name of the oldest employee
select emp.first_name,birth_date
from
employees as emp
where
emp.birth_date = (select min(birth_date) from employees );

-- 15 - get the name of the earilest hired employee
select emp.first_name,hire_date
from
employees as emp
where
emp.hire_date = (select min(hire_date) from employees );

-- 16 - get the employees names who have title senior engineer
select emp.first_name
from 
employees as emp
inner join
titles as t on emp.emp_no = t.emp_no 
where
t.title ='Senior Engineer';




