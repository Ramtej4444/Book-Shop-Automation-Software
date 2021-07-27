import sqlite3
from tkinter import messagebox
# connect to database
conn = sqlite3.connect('bookshop.db')
c = conn.cursor()


class PublisherDB:

    def add_publisher(self, publisher_):
        try:
            if self.search_publisherbyid(publisher_.get_publisherId()):
                messagebox.showinfo("success", "Publisher is registered")
                return
            else:
                c.execute("INSERT INTO Publishers(publisherName,vendorid) VALUES (?,?)",
                          [publisher_.get_publisherName(), publisher_.get_vendor()])
                conn.commit()
        except Exception as e:
            print("error --- " + str(e))



    def get_publisherbyid(self, id):
        try:
            c.execute("SELECT * FROM Publishers WHERE publisherId=?", [id])
            publisher_ = c.fetchall()
            conn.commit()
            return publisher_
        except Exception as e:
            print("error --- " + str(e))


    def search_publisherbyid(self, id):
        try:
            c.execute("SELECT * FROM Publishers WHERE publisherId=?", [id])
            publisher_ = c.fetchall()
            conn.commit()
            if publisher_ == None:
                return False
            else:
                return True

        except Exception as e:
            print("error --- " + str(e))
