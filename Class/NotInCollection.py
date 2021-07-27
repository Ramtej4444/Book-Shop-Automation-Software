# self class contains "requests" for books that are not sold in the shop

class NotInCollection:
    def __init__(self, noOfRequests=1, requestId=None, bookTitle=None, authorName=None, publisherName=None,
                 ISBNCode=None):
        self.noOfRequests = noOfRequests
        self.requestId = requestId
        self.bookTitle = bookTitle
        self.authorName = authorName
        self.publisherName = publisherName
        self.ISBNCode = ISBNCode

    def get_noofrequests(self):
        return self.noOfRequests

    def get_requestid(self):
        return self.requestId

    def set_requestid(self, requestId):
        self.requestId = requestId

    def set_noofrequests(self, noofrequests):
        self.noOfRequests = noofrequests

    def get_booktitle(self):
        return self.bookTitle

    def set_booktitle(self, bookTitle):
        self.bookTitle = bookTitle

    def get_authorname(self):
        return self.authorName

    def set_authorname(self, authorName):
        self.authorName = authorName

    def get_publishername(self):
        return self.publisherName

    def set_publishername(self, publisherName):
        self.publisherName = publisherName

    def get_isbncode(self):
        return self.ISBNCode

    def set_isbncode(self, iSBNCode):
        self.ISBNCode = iSBNCode
