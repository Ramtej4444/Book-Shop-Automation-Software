from datetime import date


class Transaction:
    def __init__(self, transactionId=None, dateOfTransaction=None, bookISBN=None, noOfCopies=1, name=None, mobile=None,paid=False):
        self.transactionId = transactionId
        self.dateOfTransaction = dateOfTransaction
        self.bookISBN = bookISBN
        self.noOfCopies = noOfCopies
        self.name = name
        self.mobile = mobile
        self.paid=paid


    def get_transactionid(self):
        return self.transactionId


    def set_transactionid(self, transactionId):
        self.transactionId = transactionId


    def get_dateoftransaction(self):
        return self.dateOfTransaction


    def set_dateoftransaction(self, dateOfTransaction):
        self.dateOfTransaction = dateOfTransaction


    def get_bookisbn(self):
        return self.bookISBN


    def set_bookisbn(self, bookISBN):
        self.bookISBN = bookISBN


    def get_noofcopies(self):
        return self.noOfCopies


    def set_noofcopies(self, noOfCopies):
        self.noOfCopies = noOfCopies


    def get_name(self):
        return self.name


    def set_name(self, name):
        self.name = name


    def get_mobile(self):
        return self.mobile


    def set_mobiles(self, mobile):
        self.mobile = mobile

    def get_paid(self):
        return self.paid


    def set_paid(self, paid):
        self.paid = paid
