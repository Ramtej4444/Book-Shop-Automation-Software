import sqlite3
from Class import NotInCollection
# connect to database
conn = sqlite3.connect('bookshop.db')
c = conn.cursor()


class NotInCollectionDB:
    def add_request(self, request):
        try:
            c.execute("SELECT * FROM NotInCollection WHERE ISBNCode=?", [request.get_isbncode()])
            R=[]
            R = c.fetchall()
            conn.commit()
            if not len(R):
                c.execute("INSERT INTO NotInCollection(noOfRequests,bookTitle,authorName,publisherName,ISBNCode) VALUES (?,?,?,?,?)",
                          [request.get_noofrequests(),  request.get_booktitle(),
                           request.get_authorname(), request.get_publishername(), request.get_isbncode()])
                conn.commit()

            else:
                for r in R:
                    c.execute("UPDATE NotInCollection SET noOfRequests=? WHERE ISBNCode=?",
                              [r[1]+1, r[5]])
                    conn.commit()

        except Exception as e:
            print("error --- " + str(e))


    def remove_request(self, ISBN_):
        try:
            c.execute("DELETE from NotInCollection WHERE ISBNCode=?", [ISBN_])
            conn.commit()

        except Exception as e:
            print("error --- " + str(e))


    # Function that helps view requests based on descending number of requests.
    # if list is null , then CHECK and give error message.
    def view_requests(self):
        try:
            c.execute("SELECT * FROM NotInCollection ORDER BY noofrequests DESC")
            R = c.fetchall()
            conn.commit()
            return R
        except Exception as e:
            print("error --- " + str(e))
