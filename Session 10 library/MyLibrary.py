class Book:
    def __init__(self, name: str, author: str, ISBN: int):
        self.name: str = name
        self.author: str = author
        self.ISBN: int = ISBN


class LibraryMember:
    def __init__(self, code: int, name: str):
        self.name: str = name
        self.code: int = code


class Library:
    def __init__(self, name: str):
        self.name: str = name
        self.__books: list[Book] = []
        self.__lend: dict[LibraryMember, list[Book]] = {}
        self.__members: dict[int, LibraryMember] = {}

    def addBook(self, book: Book):
        if type(book.ISBN) == int:
            for e in self.__books:
                if e.ISBN == book.ISBN:
                    print(f"This ISBN exists before {e.ISBN} , {e.name}, {e.author}",flush=True)
                    break
            else:
                self.__books.append(book)
                
        else:
            print("invalid ISBN Number",flush=True)

    def availableBooks(self):
        print("Books Available :")
        if len(self.__books)>0:
            for e in self.__books:
                print(f"ISBN: {e.ISBN} ,Name: {e.name} ,Author: {e.author}",flush=True)
        else:
            print("No books in the library.",flush=True)

    def __getBook(self,ISBN:int,books:list[Book]):
        found_book = [book for book in books if book.ISBN == ISBN]
        if len(found_book)>0:
            return found_book[0]
        return None 

    def addMember(self, member: LibraryMember):
        for v in self.__members.values():
            if v.code == member.code or v.name == member.name:
                print(f"this member exists before with this information: code {v.code} , name {v.name}",flush=True)
                break
        else:
            self.__members[member.code] = member

    def getMember(self, code: int):
        return self.__members.get(code)

    def lendBook(self,memberCode:int,bookISBN:int):
        book = self.__getBook(bookISBN,self.__books)
        member =self.getMember(memberCode)
        if book is None:
            print("book not exists",flush=True)
        if member is None:
            print("member not exists",flush=True)
        if book != None and member != None:
            if member in self.__lend:
                self.__lend[member].append(book)
            else:
                self.__lend.update({member:[book]})
            self.__books.remove(book)

    def ShowLendBook(self,memberCode:int):
        member =self.getMember(memberCode)        
        if member is None:
            print("member not exists",flush=True)
        if member != None:
            print(f"member {member.code} {member.name} borrowed :",flush=True)
            if member in self.__lend:
                for e in self.__lend[member]:
                    print(f"ISBN: {e.ISBN} name: {e.name} author:{e.author}",flush=True)
            else:
                print("empty",flush=True)
           
            

    def returnBorrowedBook(self,memberCode:int,bookISBN:int):
        isValid= False
        member =self.__members.get(memberCode)
        book:Book=None
        if member is None:
            print("member not exists",flush=True)
        elif self.__lend.get(member) is None:
            print("this member didn't borrow any books",flush=True)
        else:
            books = self.__lend.get(member)
            book = self.__getBook(bookISBN,books)
            if book is None:
                 print("this book not borrowed by this member",flush=True)
            else:
                isValid = True
        
        if isValid:
            self.__books.append(book)
            self.__lend[member].remove(book)
            if len(self.__lend[member]) ==0:
                self.__lend.pop(member)


            





