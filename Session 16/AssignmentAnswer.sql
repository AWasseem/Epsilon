-- github 

/*******************************************************/
/* find the number of availalbe copies of the book (Dracula)      */
/*******************************************************/
select b.Title,count(Title) as TotalAvailableCopies
from
books as b
where
b.BookID not in (select l.BookID from loans as l where l.ReturnedDate is  null)
and 
b.Title = 'Dracula'
group by b.Title;

/*******************************************************/
/* Add new books to the library                        */
/*******************************************************/
insert into books(BookID,Title,Author,Published,Barcode)
values (201,'MY Book','Abdelrahman',2025,11111);

/*******************************************************/
/* Check out Books: books(4043822646, 2855934983) whose patron_email(jvaan@wisdompets.com), loandate=2020-08-25, duedate=2020-09-08, loanid=by_your_choice*/
/*******************************************************/
insert into loans(LoanID,BookID,PatronID,LoanDate,DueDate,ReturnedDate)
 values 
 (2001,93,50,'2020-08-25','2020-09-08',null)
 ,(2002,11,50,'2020-08-25','2020-09-08',null);
 
 
/********************************************************/
/* Check books for Due back                             */
/* generate a report of books due back on July 13, 2020 */
/* with patron contact information                      */
/********************************************************/
select b.*,l.DueDate,p.*
from 
books as b
inner join
loans as l on l.BookID = b.BookID
inner join
patrons as p on p.PatronID = l.PatronID
where
l.DueDate <= '2020-7-13' and l.ReturnedDate is null;

/*******************************************************/
/* Return books to the library (which have barcode=6435968624) and return this book at this date(2020-07-05)                    */
/*******************************************************/
update loans as l
inner join
books as b on b.BookID = l.BookID
set l.ReturnedDate = '2020-07-05'
where
b.Barcode ='6435968624' and l.ReturnedDate is null;

/*******************************************************/
/* Encourage Patrons to check out books                */
/* generate a report of showing 10 patrons who have
checked out the fewest books.                          */
/*******************************************************/
select p.PatronID,p.FirstName,p.LastName,p.Email,count(l.BookID) as NoOFLoansBooks
from
patrons p
left join
loans l on l.PatronID = p.PatronID
left join
books b on b.BookID=l.BookID
group by p.PatronID
order by count(l.BookID)
limit 10;


/*******************************************************/
/* Find books to feature for an event                  
 create a list of books from 1890s that are
 currently available                                    */
/*******************************************************/
select *
from
books b
where
b.BookID not in (select l.BookID from loans l where l.ReturnedDate is null)
and 
b.Published = 1890;

/*******************************************************/
/* Book Statistics 
/* create a report to show how many books were 
published each year.                                    */
/*******************************************************/
SELECT Published, COUNT(DISTINCT(Title)) AS TotalNumberOfPublishedBooks FROM Books
GROUP BY Published
ORDER BY TotalNumberOfPublishedBooks DESC;


/*************************************************************/
/* Book Statistics                                           */
/* create a report to show 5 most popular Books to check out */
/*************************************************************/
SELECT b.Title, b.Author, b.Published, COUNT(b.Title) AS TotalTimesOfLoans FROM Books b
JOIN Loans l ON b.BookID = l.BookID
GROUP BY b.Title
ORDER BY 4 DESC
LIMIT 5;

