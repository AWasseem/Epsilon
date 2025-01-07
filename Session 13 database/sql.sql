#Try to Insert 10 rows in our database and query them using select command
use school;
insert into students(student_id,name,age,phone_number,adresse,level)
values
(1,'abderahman',30,'11111','a1',1),
(2,'ahmed',10,'11111','a1',1),
(3,'sayed',40,'11111','a1',1),
(4,'ali',10,'11111','a1',1),
(5,'badr',10,'11111','a1',1),
(6,'mohamed',10,'11111','a1',1),
(7,'mohsen',10,'11111','a1',1),
(8,'gada',10,'11111','a1',1),
(9,'helen',10,'11111','a1',1),
(10,'amira',10,'11111','a1',1);

select * from students;

