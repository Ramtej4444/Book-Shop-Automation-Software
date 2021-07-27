import sqlite3

conn=sqlite3.connect('bookshop.db')
c = conn.cursor()

'''c.execute("""CREATE TABLE books(
           bookTitle text,
           authorName text,
           price integer,
           ISBN integer  PRIMARY KEY     NOT NULL,
           noOfCopies integer,
           rackNo integer,
           noOfRequests integer,
           averageDays integer,
           threshold integer
        )""")
conn.commit()
c.execute("""CREATE TABLE NotInCollection(
           requestId integer  PRIMARY KEY     AUTOINCREMENT,
           noOfRequests integer,
           bookTitle text,
           authorName text,
           publisherName text,
           ISBNCode integer

        )""")
conn.commit()

c.execute("""CREATE TABLE Publishers(
           publisherId integer PRIMARY KEY     AUTOINCREMENT,
           publisherName text,
           vendorid  text
        )""")
conn.commit()

c.execute("""CREATE TABLE Transactions(
            transactionId integer PRIMARY KEY     AUTOINCREMENT,
            bookISBN integer,
            noOfCopies integer,
            dateOfTransaction text,
            name text,
            mobile text,
            paid BOOL
        )""")
conn.commit()

c.execute("""CREATE TABLE Vendors(
           vendorId integer PRIMARY KEY     AUTOINCREMENT,
           vendorName text,
           vendorAddress text,
           vendorEmail text
        )""")
conn.commit()

c.execute("""CREATE TABLE Employees(
      		 id integer PRIMARY KEY     AUTOINCREMENT,
             name text,
  		     userName text,
  		     password text,
  		     empCode integer
        )""")

conn.commit()

#[(12, 'tom', 'tommy', 'jerry', 3), (13, 'jerry', 'jerr', 'tom', 2)]
c.execute(" INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?)",["spidy",'stanlee','350','30012','10','1','10','10','10'])

conn.commit()

c.execute(" INSERT INTO NotInCollection (noOfRequests,bookTitle,authorName,publisherName,ISBNCode) VALUES (1,'harrypotter','r.k.rowling','rkpublisher',123456)")

conn.commit()
'''

c.execute("SELECT * FROM Publishers")
x=c.fetchall()
print(x)
conn.commit()
'''
c.execute("INSERT INTO Publishers((publisherName,vendorid))")
print(c.fetchall())
conn.commit()


c.execute(" INSERT INTO books  Vendors ('Relativity the special and generan theory','albert einstein',180,97881,1,1,2,10,10)")

conn.commit()'''
