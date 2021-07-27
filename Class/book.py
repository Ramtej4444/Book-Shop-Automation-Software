class Book:

    def __init__(self,bookTitle = '',authorName = '',price =0,ISBN =0,noOfCopies =0,rackNo =0,noOfRequests =0,averageDays =0,threshold = 0):
        self.bookTitle = bookTitle
        self.authorName = authorName
        self.price = price
        self.ISBN = ISBN
        self.noOfCopies = noOfCopies
        self.rackNo = rackNo
        self.noOfRequests = noOfRequests
        self.averageDays = averageDays
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, thres=None):
        self.threshold = thres

    def get_averagedays(self):
        return self.averageDays

    def set_averagedays(self, avgdays=None):
        self.averageDays = avgdays

    def get_booktitle(self):
        return self.bookTitle

    def set_booktitle(self, title=None):
        self.bookTitle = title

    def set_authorname(self, name=None):
        self.authorName = name

    def get_authorname(self):
        return self.authorName

    def get_price(self):
        return self.price

    def set_price(self, prc=None):
        self.price = prc

    def get_isbn(self):
        return self.ISBN

    def set_isbn(self, isbn=None):
        self.ISBN = isbn

    def get_noofcopies(self):
        return self.noOfCopies

    def set_noofcopies(self, copies=None):
        self.noOfCopies = copies

    def get_rackno(self):
        return self.rackNo

    def set_rackno(self, no=None):
        self.rackNo = no

    def get_noofrequests(self):
        return self.noOfRequests

    def set_noofrequests(self, requests=None):
        self.noOfRequests = requests