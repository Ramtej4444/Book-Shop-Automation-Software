from DataBaseClass import NotInCollectionDB, TransactionDB
from Class import Employee


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.empCode = 2

    # this helps viewing the requests
    def viewRequests(self):
        # connect to data base and print all
        requests = NotInCollectionDB().view_requests()
        R = "REQUESTS \n"
        i = 0
        # request_id , noOfRequests, bookTitle,, authorName, publisherName, ISBNCode, primary key(request_id)
        for r in requests:
            i=i+1
            R = R + "\n" + str(i) + ".ISBNcode: " + str(r[5])
            R = R + "\n  BookTitle: " + str(r[2])
            R = R + "\n  AuthorName: " + str(r[3])
            R = R + "\n  No. of requests: " + str(r[1])

        return R
    def viewStatistics(self, fromdate, todate):
        x = TransactionDB().get_statistics(fromdate, todate)
        return x
