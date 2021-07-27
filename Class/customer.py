from DataBaseClass import BookDB
from DataBaseClass import NotInCollectionDB
from Class import NotInCollection


class Customer:
    def __init__(self):
        self.books_cart = []

    def add_books(self, noofcopies=1, thebook=None):
        isbn = thebook.get_isbn()
        for b in self.books_cart:
            if b[0].get_isbn() == isbn:
                b[1] = noofcopies + b[1]
                return
        self.books_cart.append((thebook, noofcopies))

    def edit_cart(self, thebook, noofcopies):
        isbn = thebook.get_isbn()
        for b in self.books_cart:
            if b[0].get_isbn() == isbn:
                if b[1] <= noofcopies:
                    self.books_cart.remove(b)
                else:
                    b[1] = b[1] - noofcopies
                return

    def return_cart(self):
        return self.books_cart

    def searchbytitle(self, title):
        bookslist = BookDB().get_bookbytitle(title)
        return bookslist

    def searchbyauthor(self, author):
        bookslist = BookDB().get_bookbyauthorname(author)
        return bookslist

    def incrementrequestfield(self, bookTitle, authorName, ISBNCode):
        req = NotInCollection(1, None, bookTitle, authorName, None, ISBNCode)
        NotInCollectionDB().add_request(req)
        return
