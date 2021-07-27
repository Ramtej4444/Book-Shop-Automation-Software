import sqlite3
from tkinter import messagebox
# connect to database
conn = sqlite3.connect('bookshop.db')
c = conn.cursor()


class VendorDB:

    def get_vendorbyid(self, id):
        try:
            c.execute("SELECT * FROM Vendors WHERE vendorId=?", [id])
            vendor_ = c.fetchall()
            conn.commit()
            return vendor_
        except Exception as e:
            print("error --- " + str(e))
            return None

    def search_vendorbyid(self, id):
        try:
            c.execute("SELECT * FROM Vendors WHERE vendorId=?", [id])
            vendor_ = c.fetchall()
            conn.commit()
            if vendor_ == None:
                return False
            else:
                return True
        except Exception as e:
            print("error --- " + str(e))
            return None

    def add_vendor(self, vendor_):
        try:
            if (self.search_vendorbyid(vendor_.get_id())):
                messagebox.showinfo("success", "Vendor is registered")
                return
            else:
                c.execute("INSERT INTO Vendors(vendorName,vendorAddress,vendorEmail) VALUES (?,?,?)",
                          [ vendor_.get_name(), vendor_.get_address(), vendor_.get_email()])
                conn.commit()
                print("Vendor added! " + str(vendor_.get_id()))
        except Exception as e:
            print("error --- " + str(e))
            return None
