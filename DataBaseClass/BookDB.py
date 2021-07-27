import sqlite3
from DataBaseClass import NotInCollectionDB, TransactionDB
from Class import Book
from tkinter import messagebox

# connect to database
conn = sqlite3.connect('bookshop.db')
c = conn.cursor()


class BookDB:

    def add_book(self, thebook, quantity):
        quantity=int(quantity)
        print([thebook.get_booktitle(), thebook.get_authorname(), thebook.get_price(), thebook.get_isbn(),
        thebook.get_noofcopies(), thebook.get_rackno(), thebook.get_noofrequests(),
        thebook.get_averagedays(), thebook.get_threshold()])
        try:
            ISBN_ = thebook.get_isbn()
            c.execute("SELECT * FROM books WHERE ISBN=?", [ISBN_])
            B = c.fetchall()
            conn.commit()

            if not len(B):
                #NotInCollectionDB().remove_request(ISBN_)
                print(1)
                thebook.set_noofcopies(quantity)

                c.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?)",
                          [thebook.get_booktitle(), thebook.get_authorname(), thebook.get_price(), thebook.get_isbn(),
                           thebook.get_noofcopies(), thebook.get_rackno(), thebook.get_noofrequests(),
                           thebook.get_averagedays(), thebook.get_threshold()])
                conn.commit()
                return

            if (int(thebook.get_noofcopies()) + quantity) < 0:
                messagebox.showerror("Error", "InValid no. of copies")
                return

            thebook.set_noofcopies(int(thebook.get_noofcopies())+ quantity)
            c.execute("UPDATE books SET noofcopies=? WHERE ISBN=?", [thebook.get_noofcopies(), ISBN_])
            conn.commit()

        except Exception as e:
            print("error ---1 " + str(e))
            return

    def delete_book(self, ISBN_):
        c.execute("SELECT * FROM books WHERE ISBN=?", [ISBN_])
        B = c.fetchall()
        conn.commit()
        if not len(B):
            messagebox.showerror("Error", "Book Doesn't exist")
            return
        book = Book(B)
        if book.get_noofcopies() == 0:
            messagebox.showerror("Error", " No copies are present for deletion")
            return

        try:
            book.set_noofcopies(book.get_noofcopies() - 1)
            c.execute("UPDATE books SET noOfCopies=? WHERE ISBN=?", [book.get_noofcopies(), ISBN_])
            c.commit()
            messagebox.showinfo("success", "Book Added")

        except Exception as e:
            print("error --- 2" + str(e))
            return

    def get_bookbytitle(self, title):

        c.execute("SELECT * FROM books WHERE bookTitle=?", [title])
        bookList = c.fetchall()

        booksList = []
        for book in bookList:
            B = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
            booksList.append(B)
        conn.commit()
        return booksList

    def get_bookbyauthorname(self, authorname):
        c.execute("SELECT * FROM books WHERE authorName=?", [authorname])
        bookList = c.fetchall()
        booksList = []
        for book in bookList:
            B = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
            booksList.append(B)
        conn.commit()
        return booksList

    def does_bookexist(self, ISBN_):
        c.execute("SELECT * FROM books WHERE ISBN=?", [ISBN_])
        B = c.fetchall()
        conn.commit()
        if not len(B):
            return False
        return True

    def get_bookbyisbn(self, ISBN_):
        c.execute("SELECT * FROM books WHERE ISBN=?", [ISBN_])
        book = c.fetchall()
        conn.commit()
        book = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
        return book

    def update_requests(self, thebook):
        try:
            c.execute("SELECT * FROM books WHERE ISBN=?", [thebook.get_isbn()])
            book = c.fetchall()
            Book_ = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
            c.commit()
            Book_.set_noofrequests(Book_.get_noofrequests() + 1)
            c.execute("UPDATE books SET noOfCopies=? WHERE ISBN=?", [Book_.get_noofcopies(), thebook.get_isbn()])
            conn.commit()

        except Exception as e:
            print("error ---3 " + str(e))
            return None

    def get_requests(self):
        try:
            c.execute("SELECT * FROM books WHERE noOfCopies>0 ORDER BY noOfRequests DESC")
            bookList = c.fetchall()
            booksList = []
            for book in bookList:
                B = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
                booksList.append(B)
            conn.commit()
            return booksList

        except Exception as e:
            print("error --- 4" + str(e))
            return None



    def get_inventorylevel(self, ISBN_):
        try:
            c.execute("SELECT * FROM books WHERE ISBN=?", [ISBN_])
            B = c.fetchall()
            if not len(B):
                messagebox.showerror("Error", "Book Doesn't Exist")
                return

            else:
                book=B[0]
                book_ = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
                no = TransactionDB().get_noofcopiessold(ISBN_)
                return no * book_.get_averagedays()

        except Exception as e:
            print("error ---5 " + str(e))
            return None

    def get_booksbelowthreshold(self):
        try:
            c.execute("SELECT * FROM books WHERE noOfCopies<threshold")
            bookList = c.fetchall()
            booksList = []
            for book in bookList:
                B = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
                booksList.append(B)
            conn.commit()
            return booksList

        except Exception as e:
            print("error ---6 " + str(e))
            return None
