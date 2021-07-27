import sqlite3
from Class import Book,Transaction
from tkinter import messagebox
from datetime import date
# connect to database
conn = sqlite3.connect('bookshop.db')
c = conn.cursor()


class TransactionDB:
    def add_transaction(self,transaction_):
        try:
            c.execute("INSERT INTO Transactions(bookISBN,noOfCopies,dateOfTransaction ,name ,mobile,paid ) VALUES (?,?,?,?,?,?)",
                      [transaction_.get_bookisbn(), transaction_.get_noofcopies()
                      ,transaction_.get_dateoftransaction(),transaction_.get_name(),transaction_.get_mobile(),transaction_.get_paid()])
            conn.commit()
        except Exception as e:
            print("error --- " + str(e))
            messagebox.showerror("Error", "Error while transaction")

    def get_transactionbyid(self,id):
        try:
            c.execute("SELECT * FROM Transactions WHERE ID=?", [id])
            transaction_ = c.fetchall()
            conn.commit()
            return transaction_

        except Exception as e:
            print("error --- " + str(e))
            return None

    def get_statistics(self,fromdate, todate):

        try:
            c.execute("SELECT * FROM Transactions WHERE paid =?",[True])
            R = c.fetchall()
            conn.commit()
            results=[]
            for r in R:
                fromtext=r[3]
                fy = fromtext[0] + fromtext[1] + fromtext[2] + fromtext[3]
                fm = fromtext[5] + fromtext[6]
                fd = fromtext[8] + fromtext[9]
                f = date(int(fy), int(fm), int(fd))
                if f<=todate and f>=fromdate:
                    results.append(r)

            if not len(results):
                return " No Requests"
            global strng
            k = 0
            strng = "RESULTS:\n\n"
            ls=set()
            for x in results:
                if not(x[1] in ls):
                    k=k+1
                    ls.add(x[1])
                    SalesRevenue=0
                    bname=''
                    aname=''
                    isbn=x[1]
                    price=0
                    for r in results:
                        if x[1]==r[1]:
                            c.execute("SELECT * FROM Books WHERE ISBN=?", [x[1]])
                            B =c.fetchall()
                            conn.commit()
                            book=B[0]
                            book=Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
                            price = book.get_price()
                            SalesRevenue = SalesRevenue + r[2] * price
                            bname=book.get_booktitle()
                            aname=book.get_authorname()
                    cop=SalesRevenue/price
                    strng = strng + str(k) + ".BookName:" + str(bname) + "\nAuthorName:" + str(aname)
                    strng = strng + "\nISBN:" + str(isbn) + "\nCopies Sold:" + str(cop) + "\nSales Revenue:" + str(SalesRevenue) + "\n\n"
            return strng

            


        except Exception as e:
            print("error --- " + str(e))
            return None

    def get_noofcopiessold(self,isbn_):
        try:
            c.execute("SELECT * FROM Transactions WHERE ISBN=? and paid=?", [isbn_,True])
            results = c.fetchall()
            conn.commit()
            copies = 0
            for x in results:
                copies = copies + x[3]
            return copies

        except Exception as e:
            print("error --- " + str(e))
            return None

    def set_paid(self,paid,id,copies_,isbn_):
        try:
            print(id)
            c.execute("SELECT * FROM Transactions WHERE transactionId=?",[id])
            results = c.fetchall()
            conn.commit()
            print(results)
            for x in results:
                c.execute("UPDATE Transactions SET paid=?,noOfCopies=? WHERE transactionId=?",[paid,copies_, id])
                conn.commit()
                if paid==True:
                    c.execute("SELECT * FROM books WHERE ISBN=? ", [isbn_])
                    book_ = c.fetchall()
                    conn.commit()
                    if book_[0][4]>=copies_:
                        c.execute("UPDATE books SET noOfCopies=? WHERE ISBN=?",[book_[0][4]-copies_,isbn_])
                        conn.commit()
                    else:
                        x="There are only "+str(book_[0][4])+" books left"
                        r=messagebox.showerror("Error",x)
                        if r=="ok":
                            return

        except Exception as e:
            print("error --- " + str(e))
