from tkinter import *
from tkinter import ttk
from Class import Customer, Employee, Vendor, Publisher,Book, Owner, Manager,NotInCollection,Transaction,SalesClerk
from DataBaseClass import BookDB, PublisherDB, VendorDB, TransactionDB, NotInCollectionDB
from tkinter import messagebox
from datetime import date
import sqlite3

class EmployeeFrame(Frame):
  def __init__(self, master=None,):
      Frame.__init__(self,master=None)
      self.grid(row=0, column=0, columnspan=3)
      self.master = master
      button1=Button(self.master,text="Update Inventory",font=("Helvetica",10),width=25,height=2)
      button2=Button(self.master,text="Print SalesStatistics",font=("Helvetica",10),width=25,height=2)
      button3=Button(self.master,text="View Request Field",font=("Helvetica",10),width=25,height=2)
      button4=Button(self.master,text="Checkout",font=("Helvetica",10),width=25,height=2)
      button5=Button(self.master,text="View Below Threshold",font=("Helvetica",10),width=25,height=2)
      button1.place(relx=0.5,rely=0.2,anchor=CENTER)
      button2.place(relx=0.5,rely=0.3,anchor=CENTER)
      button3.place(relx=0.5,rely=0.4,anchor=CENTER)
      button4.place(relx=0.5,rely=0.5,anchor=CENTER)
      button5.place(relx=0.5,rely=0.6,anchor=CENTER)
      button1.config(command= lambda: select_frame(updatestock,self.master))
      button2.config(command=lambda: select_frame(StatisticsFrame, self.master))
      button3.config(command=lambda: select_frame(RequestBooks, self.master))
      button4.config(command=lambda: select_frame(SalesReciept, self.master))
      button5.config(command=lambda: select_frame(ThresholdView, self.master))


class RequestBooks(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        my_label1 = Label(self.master, text="Userid:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.1, anchor=CENTER)

        Useridtext = Text(self.master, height=1,width=20)
        Useridtext.place(relx=0.5, rely=0.1, anchor=CENTER)

        my_label1 = Label(self.master, text="password:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.2, anchor=CENTER)

        passwordtext = Text(self.master, height=1,width=20)
        passwordtext.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.output = ""
        self.manager_ = Manager()
        def login( self,master):
            global Userid
            Userid = Useridtext.get(1.0, END)
            global password
            password = passwordtext.get(1.0, END)
            Userid = Userid.replace('\n', '')
            password = password.replace('\n', '')
            self.master = master
            for item in self.master.winfo_children():
                item.destroy()
            conn = sqlite3.connect('bookshop.db')
            c = conn.cursor()
            c.execute("SELECT * from Employees WHERE id=? and password=?  and empCode>1", [Userid, password])
            employeelist = c.fetchall()
            conn.commit()
            if not len(employeelist):
                r = messagebox.showerror("error", "INVALID login details")
                if r == "ok":
                    logout(self.master)
            support = Frame(self.master)
            support.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.label = Label(support, text="Request Field", width=25, height=2)
            self.label.pack()
            self.textbox = Text(support, width=40, height=25)
            self.textbox.pack()
            self.logoutbut = Button(support, text="Logout", width=12, height=2, command=lambda: logout(self.master))
            self.logoutbut.pack()
            self.output = self.manager_.viewRequests()
            self.textbox.insert(END, self.output)

        loginButton = Button(self.master, text="Login", font=("Helvetica", 10), width=20, height=2, bg='green',
                             command=lambda: login(self, self.master))
        loginButton.place(relx=0.5, rely=0.4, anchor=CENTER)
'''  def __init__(self, master=None):
      Frame.__init__(self,master=None)
      self.grid(row=0,column=0,columnspan=3)
      self.master = master'''




class ThresholdView(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master

        my_label1 = Label(self.master, text="Userid:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.1, anchor=CENTER)

        Useridtext = Text(self.master, height=1,width=20)
        Useridtext.place(relx=0.5, rely=0.1, anchor=CENTER)

        my_label1 = Label(self.master, text="password:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.2, anchor=CENTER)

        passwordtext = Text(self.master, height=1,width=20)
        passwordtext.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.output = ""
        self.owner_ = Owner()
        def login(self, master):
            global Userid
            Userid = Useridtext.get(1.0, END)
            global password
            password = passwordtext.get(1.0, END)
            Userid = Userid.replace('\n', '')
            password = password.replace('\n', '')
            self.master = master
            for item in self.master.winfo_children():
                item.destroy()
            conn = sqlite3.connect('bookshop.db')
            c = conn.cursor()
            c.execute("SELECT * from Employees WHERE id=? and password=? and empCode>2", [Userid, password])
            employeelist = c.fetchall()
            conn.commit()
            emp = None
            if not len(employeelist):
                r = messagebox.showerror("error", "INVALID login details")
                if r == "ok":
                    logout(self.master)
            emp = employeelist[0]


            self.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.innerframe2 = Frame(self.master)
            self.innerframe2.pack()
            self.user = ""
            self.userlabel = Label(self.innerframe2, height=2, width=25, text="" + self.user)
            self.userlabel.pack(side="left")
            self.logout = Button(self.innerframe2, width=10, height=2, text="Logout",
                                 command=lambda: logout(self.master))
            self.logout.pack(side="right")
            self.label = Label(self.master, bg="lightgreen", fg="black", text="Books Below Threshold")
            self.label.config(height=3, width=25)
            self.label.pack()
            self.threshold = Text(self.master, height=25, width=60, padx=2, pady=2)
            self.threshold.pack()
            self.viewbutton = Button(self.master, bg="yellow", fg="black", height=3, width=12,
                                     text="View", command=lambda:viewthreshold())
            self.viewbutton.pack()
            def viewthreshold():
                output = self.owner_.viewThreshold()
                self.threshold.insert(END, output)
        loginButton = Button(self.master, text="Login", font=("Helvetica", 10), width=20, height=2, bg='green',
                             command=lambda: login(self, self.master))
        loginButton.place(relx=0.5, rely=0.4, anchor=CENTER)
    '''def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master= master'''



class StatisticsFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master

        my_label1 = Label(self.master, text="Userid:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.1, anchor=CENTER)

        Useridtext = Text(self.master, height=1,width=20)
        Useridtext.place(relx=0.5, rely=0.1, anchor=CENTER)

        my_label1 = Label(self.master, text="password:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.2, anchor=CENTER)

        passwordtext = Text(self.master, height=1,width=20)
        passwordtext.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.manager_ = Manager()
        def login(self, master):
            global Userid
            Userid = Useridtext.get(1.0, END)
            global password
            password = passwordtext.get(1.0, END)
            Userid = Userid.replace('\n', '')
            password = password.replace('\n', '')
            self.master = master
            for item in self.master.winfo_children():
                item.destroy()
            conn = sqlite3.connect('bookshop.db')
            c = conn.cursor()
            c.execute("SELECT * from Employees WHERE id=? and password=? and empCode>1", [Userid, password])
            employeelist = c.fetchall()
            conn.commit()
            emp = None
            if not len(employeelist):
                r = messagebox.showerror("error", "INVALID login details")
                if r == "ok":
                    logout(self.master)
            emp = employeelist[0]
            global employee
            employee = Employee(emp[1], emp[2], emp[3], emp[0])
            support = Frame(self.master)
            support.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.innerframe2 = Frame(support)
            self.innerframe2.grid(row=0, column=0, columnspan=2)
            self.user = ""
            self.userlabel = Label(self.innerframe2, height=2, width=25, text="" + self.user)
            self.userlabel.pack(side="left")
            self.logout = Button(self.innerframe2, width=10, height=2, text="Logout",
                                 command=lambda: logout(self.master))
            self.logout.pack(side="right")
            self.startdate = Label(support, text="Enter From Date:", fg="black", bg="yellow",
                                   height=2, width=20)
            self.startdate.grid(row=1, column=0)
            self.enddate = Label(support, text="Enter Last Date:", fg="black", bg="yellow",
                                 height=2, width=20)
            self.enddate.grid(row=2, column=0)
            self.entrystart = Text(support, width=20, height=1)
            self.entrystart.grid(row=1, column=1, padx=10)
            self.entrylast = Text(support, height=1, width=20)
            self.entrylast.grid(row=2, column=1)
            self.viewstats = Button(support, height=2, width=10, text="Get Statistics"
                                    ,command=lambda:viewbutton())
            self.viewstats.grid(row=3, column=0, columnspan=2)
            self.View = Label(support, text="SalesStatistics:", fg="black", bg="lightgreen",
                              height=2, width=25)
            self.View.grid(row=4, column=0, columnspan=2)
            self.viewbox = Text(support, bg="white", fg="black", padx=5, pady=5, height=20, width=40)
            self.viewbox.grid(row=5, column=0, columnspan=2)
            self.output = ""
            def viewbutton():
                fromtext = self.entrystart.get(1.0, END)
                lasttext = self.entrylast.get(1.0, END)

                fy = fromtext[0] + fromtext[1] + fromtext[2] + fromtext[3]
                fm = fromtext[5] + fromtext[6]
                fd = fromtext[8] + fromtext[9]

                try:
                    f = date(int(fy), int(fm), int(fd))
                except Exception as e:
                    messagebox.showerror("Error","Invalid from date")
                ty = lasttext[0] + lasttext[1] + lasttext[2] + lasttext[3]
                tm = lasttext[5] + lasttext[6]
                td = lasttext[8] + lasttext[9]

                try:
                    t = date(int(ty), int(tm), int(td))
                except Exception as e:
                    messagebox.showerror("Error","Invalid from date")
                self.output = self.manager_.viewStatistics(f,t)
                self.viewbox.insert(END, self.output)


        loginButton = Button(self.master, text="Login", font=("Helvetica", 10), width=20, height=2, bg='green',
                             command=lambda: login(self, self.master))
        loginButton.place(relx=0.5, rely=0.4, anchor=CENTER)
    '''def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master=master'''

class Procurement(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=None)
        self.master=master

        my_lab=Label(self.master,text="Fill in these details for the Procurement form:",font=("Helvetica",10))
        my_lab.grid(row=0,column=1,pady=2)

        my_label1=Label(self.master,text="BookTitle:",font=("Helvetica",10),width=20,height=2)
        my_label1.grid(row=1,column=0,pady=2)

        BookTitle=Text(self.master,height=1)
        BookTitle.grid(row=1,column=1,pady=2)

        my_label1=Label(self.master,text="AuthorName:",font=("Helvetica",10),width=20,height=2)
        my_label1.grid(row=2,column=0,pady=2)

        AuthorName=Text(self.master,height=1)
        AuthorName.grid(row=2,column=1,pady=2)

        my_label1=Label(self.master,text="Publisher:",font=("Helvetica",10),width=20,height=2)
        my_label1.grid(row=3,column=0,pady=2)

        Publisher=Text(self.master,height=1)
        Publisher.grid(row=3,column=1,pady=2)

        my_label1=Label(self.master,text="ISBN:",font=("Helvetica",10),width=20,height=2)
        my_label1.grid(row=4,column=0,pady=2)

        ISBN=Text(self.master,height=1)
        ISBN.grid(row=4,column=1,pady=2)

        def Order():
            BookTitle_ = BookTitle.get(1.0,END)
            BookTitle_=BookTitle_.replace('\n', '')

            AuthorName_ = AuthorName.get(1.0,END)
            AuthorName_=AuthorName_.replace('\n', '')

            Publisher_ = Publisher.get(1.0,END)
            Publisher_=Publisher_.replace('\n', '')

            ISBN_ = ISBN.get(1.0,END)
            ISBN_=ISBN_.replace('\n', '')

            #noOfRequests=1,requestId=None,bookTitle=None,authorName=None,publisherName=None,ISBNCode=None
            pro=NotInCollection(1,None,BookTitle_,AuthorName_,Publisher_,ISBN_)

            NotInCollectionDB().add_request(pro)

            r=messagebox.showinfo("Request","Request added Successfully")
            if r=="ok":
                self.master.destroy()




        orderButton=Button(self.master,text="place order",font=("Helvetica",10),width=20,height=2,bg='green',command=Order)
        orderButton.grid(row=6,column=1,pady=2)



class CustomerFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.grid(row=0, column=0, columnspan=3)
        Search = Label(self.master, text="Enter your name:", font=("Helvetica", 10))
        Search.grid(row=0, column=0, pady=2)
        global name
        name = Text(self.master, height=1)
        name.grid(row=0, column=1, pady=2)

        Search = Label(self.master, text="Enter your mobile NO.:", font=("Helvetica", 10))
        Search.grid(row=1, column=0, pady=2)
        global Mnum
        Mnum = Text(self.master, height=1)
        Mnum.grid(row=1, column=1, pady=2)

        Search = Label(self.master, text="Enter Title/Author name :", font=("Helvetica", 10))
        Search.grid(row=2, column=0, pady=2)
        global text_
        text_ = Text(self.master, height=1)
        text_.grid(row=2, column=1, pady=2)
        global list_
        list_ = []
        global customer_
        customer_= Customer()
        global checkout
        checkout = []
        def searchtitle():
            title = text_.get("1.0", END)
            title=title.replace('\n','')
            list_ = customer_.searchbytitle(title)
            if len(list_) == 0:
                r =messagebox.showinfo("Book not found!","Enter Details for Procurement")
                if r=="ok":
                    newwin = Toplevel()
                    frame = Procurement(newwin)

            for item in list_:
                print("----",item.get_isbn())
                Booklist.insert(END,item.get_isbn())
                s="Name:" +str(item.get_booktitle()) + "\n" +"Author:" + str(item.get_authorname())+ "\n" +"ISBN:" + str(item.get_isbn()) + "\n" +"Price" + str(item.get_price()) + "\n" +"NoofCopies available" +str(item.get_noofcopies() )+ "\n" +"Rack No" + str(item.get_rackno())

                books.insert(END,s)


        SBT = Button(self.master, text="Search by Title", font=("Helvetica", 10), width=20, height=2, bg='green',
                     command=searchtitle)
        SBT.grid(row=3, column=1, pady=5)

        def searchauthor():
            author = text_.get("1.0", END)
            author=author.replace('\n','')
            list_ = customer_.searchbyauthor(author)
            if len(list_) == 0:
                r =messagebox.showinfo("Book not found!","Enter Details for Procurement")
                if r=="ok":
                    newwin = Toplevel()
                    frame = Procurement(newwin)
            for item in list_:
                print("----",item.get_isbn())
                Booklist.insert(END,item.get_isbn())
                s="Name:" +str(item.get_booktitle()) + "\n" +"Author:" + str(item.get_authorname())+ "\n" +"ISBN:" + str(item.get_isbn()) + "\n" +"Price" + str(item.get_price()) + "\n" +"NoofCopies available" +str(item.get_noofcopies() )+ "\n" +"Rack No" + str(item.get_rackno())

                books.insert(END,s)

        SBA = Button(self.master, text="Search by Author", font=("Helvetica", 10), width=20, height=2, bg='green',
                     command=searchauthor)
        SBA.grid(row=4, column=1, pady=5)

        Booklist = Listbox(self.master, height=20, width=30)
        Booklist.grid(row=5, column=0)
        books = Text(self.master, font=("Helvetica", 10), height=20, selectbackground="yellow",
                     selectforeground="black")
        books.grid(row=5, column=1)


        def selectBook():
            tempisbn = Booklist.get(ANCHOR)
            #cart.insert(END,tempisbn)
            #checkout.append(tempisbn)
            customername = name.get(1.0,END)
            customername=customername.replace('\n','')
            customermobo = Mnum.get(1.0, END)
            customermobo=customermobo.replace('\n','')
            today = date.today()
            tran_=Transaction(None,today,tempisbn,1,customername,customermobo,False)
            print(tran_.get_bookisbn(),tran_.get_dateoftransaction())
            TransactionDB().add_transaction(tran_)


        button1 = Button(self.master, text="Checkout", font=("Helvetica", 10), width=20, height=2, bg='green',
                         command=selectBook)
        button1.grid(row=6, column=0)



        bookstext = Label(self.master, text="    Books    ", font=("Helvetica", 10), width=20, height=2, bg="yellow")
        bookstext.grid(row=6, column=1)



        '''carttext = Label(self.master, text="--Cart--", font=("Helvetica", 10), width=20, height=2, bg="yellow")
        carttext.grid(row=4, column=2)
        cart = Listbox(self.master, font=("Helvetica", 10), width=60, height=20, selectbackground="yellow",
                       selectforeground="black")
        cart.grid(row=5, column=2)
        def selectCartBook():
            cart.delete(ANCHOR)
            checkout.remove(cart.get(ANCHOR))
        editbooks = Button(self.master, text="Delete Book", font=("Helvetica", 10), width=20, height=2, bg='green',
                           command=selectCartBook)
        editbooks.grid(row=6, column=2)
        def proceedCommand(checkout):
            global customername
            global customermobo
            customername = name.get(1.0,END)
            customername=customername.replace('\n','')
            customermobo = Mnum.get(1.0, END)
            customermobo=customermobo.replace('\n','')
            print(checkout)

        proceed = Button(self.master, text="Checkout", font=("Helvetica", 10), width=20, height=2, bg='green',
                           command=lambda:proceedCommand(checkout))
        proceed.grid(row=3, column=2)'''



class finalreceipt(Frame):
    def __init__(self,rec_,master=None):
        Frame.__init__(self, master=None)
        self.master = master
        my_label1 = Label(self.master, text="Final Receipt", font=("Helvetica", 10), width=40, height=2)
        my_label1.pack()

        Receipt = Text(self.master,width=80,height=20)
        Receipt.pack()
        Receipt.insert(END,rec_)
        Receipt.config(state='disabled')
        def des(master):
            master.destroy()

        showbut=Button(self.master,text=" OK ",height=2,width=15,command=lambda:des(self.master))
        showbut.pack()

class SalesReciept(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master

        my_label1 = Label(self.master, text="Userid:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.1, anchor=CENTER)

        Useridtext = Text(self.master, height=1,width=20)
        Useridtext.place(relx=0.5, rely=0.1, anchor=CENTER)

        my_label1 = Label(self.master, text="password:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.2, anchor=CENTER)

        passwordtext = Text(self.master, height=1,width=20)
        passwordtext.place(relx=0.5, rely=0.2, anchor=CENTER)

        def login(self, master):
            global Userid
            Userid = Useridtext.get(1.0, END)
            global password
            password = passwordtext.get(1.0, END)
            Userid = Userid.replace('\n', '')
            password = password.replace('\n', '')
            self.master = master
            for item in self.master.winfo_children():
                item.destroy()
            conn = sqlite3.connect('bookshop.db')
            c = conn.cursor()
            c.execute("SELECT * from Employees WHERE id=? and password=?", [Userid, password])
            employeelist = c.fetchall()
            conn.commit()
            emp = None
            if not len(employeelist):
                r = messagebox.showerror("error", "INVALID login details")
                if r == "ok":
                    logout(self.master)
            emp = employeelist[0]
            global employee
            employee = Employee(emp[1], emp[2], emp[3], emp[0])

            support = Frame(self.master)
            support.place(relx=0.5, rely=0.5, anchor=CENTER)
            viewlabel = Label(support, text="Customer Cart", height=3, width=20,
                              bg="lightgreen", fg="black")
            viewlabel.grid(row=0, column=0, )


            cartbox = Listbox(support, height=25, width=30)
            cartbox.grid(row=1, column=0)
            cartbox.insert(END, checkout)
            self.innerframe = Frame(support)
            tranid=[]
            def showcart():
                mobile_=mobilenum.get(1.0,END)
                mobile_ = mobile_.replace('\n', '')
                c.execute("SELECT * FROM Transactions WHERE paid=? and mobile=?", [False,mobile_])
                results = c.fetchall()
                conn.commit()
                for r in results:
                    tranid.append([r[0],r[1]])
                    cartbox.insert(END,r[1])



            mobile = Label(self.innerframe, text="Mobile Number", height=2, width=15,
                               bg="cyan", fg="black")
            mobile.grid(row=0, column=0, columnspan=1)
            mobilenum = Text(self.innerframe, height=2, width=15)
            mobilenum.grid(row=1, column=0, padx=8)
            showbut=Button(self.innerframe,text=" Show ",height=2,width=15,command=lambda:showcart())
            showbut.grid(row=1,column=1,padx=5,pady=5)
            final_trans=[]
            def add():
                isbn_=isbnentry.get(1.0,END)
                isbn_ = isbn_.replace('\n', '')
                copies_=copiesentry.get(1.0,END)
                copies_ = copies_.replace('\n', '')
                id=None
                c.execute("SELECT * FROM books WHERE ISBN=?", [isbn_])
                B = c.fetchall()
                conn.commit()
                price=B[0][2]
                name=B[0][0]
                print(tranid)
                for x in tranid:
                    print(len(isbn_),isbn_)
                    if str(x[1])==isbn_:
                        print(100)
                        final_trans.append([int(isbn_),int(copies_),x[0],price,name])

                        #paid,id,copies_,isbn_
                        TransactionDB().set_paid(True,x[0],int(copies_),int(isbn_))




            def printfinal():
                rec_="\t --BILL--\n"
                total=0
                for x in final_trans:
                    p=x[1]*x[3]
                    rec_=rec_+"\n"+"Book Title:"+str(x[4])+"]\nISBN:"+str(x[0])+"\nCopies:"+str(x[1])+"\nTotal price:"+str(p)
                    total=total+p
                rec_=rec_+"\n\t"+"Final Price:"+str(total)
                print(rec_)
                newwin = Toplevel()
                frame = finalreceipt(rec_,newwin)

            self.innerframe.grid(row=1, column=1, rowspan=1)
            isbn = Label(self.innerframe, text="ISBN Number", height=2, width=15,
                         bg="cyan", fg="black")
            isbn.grid(row=2, column=0, sticky=S, rowspan=1, pady=3, padx=5)
            isbnentry = Text(self.innerframe, height=2, width=25)
            isbnentry.grid(row=2, column=1, sticky=S, padx=8)
            noofcopies = Label(self.innerframe, text="No of Copies", height=2, width=15,
                               bg="cyan", fg="black")
            noofcopies.grid(row=3, column=0, pady=3, padx=5)
            copiesentry = Text(self.innerframe, height=2, width=25)
            copiesentry.grid(row=3, column=1, padx=8)


            button1 = Button(self.innerframe, text="Add to Bill", height=2, width=10,command=lambda:add())
            button1.grid(row=4, column=0, rowspan=2)
            button2 = Button(self.innerframe, height=2, width=20, text="Print Reciept",command=lambda:printfinal())
            button2.grid(row=4, column=1, rowspan=2)
            self.innerframe2 = Frame(support)
            self.innerframe2.grid(row=0, column=1)
            self.user = ""
            self.userlabel = Label(self.innerframe2, height=2, width=25, text="" + self.user)
            self.userlabel.pack(side="left")
            self.logout = Button(self.innerframe2, width=10, height=2, text="Logout",
                                 command=lambda: logout(self.master))
            self.logout.pack(side="right")

        loginButton = Button(self.master, text="Login", font=("Helvetica", 10), width=20, height=2, bg='green',
                             command=lambda: login(self, self.master))
        loginButton.place(relx=0.5, rely=0.4, anchor=CENTER)
    '''def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master= master'''


def select_frame( typename,master):
    for child in master.winfo_children():
        child.destroy()
    new = typename(master)


def logout( master):
    for child in master.winfo_children():
        child.destroy()
    new = EmployeeFrame(master)




class updatestock(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master

        my_label1 = Label(self.master, text="Userid:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.1, anchor=CENTER)

        Useridtext = Text(self.master, height=1,width=20)
        Useridtext.place(relx=0.5, rely=0.1, anchor=CENTER)

        my_label1 = Label(self.master, text="password:", font=("Helvetica", 10), width=20, height=2)
        my_label1.place(relx=0.2, rely=0.2, anchor=CENTER)

        passwordtext = Text(self.master, height=1,width=20)
        passwordtext.place(relx=0.5, rely=0.2, anchor=CENTER)

        def login( master):
            global Userid
            Userid = Useridtext.get(1.0, END)
            global password
            password = passwordtext.get(1.0, END)
            Userid = Userid.replace('\n', '')
            password = password.replace('\n', '')
            for item in master.winfo_children():
                item.destroy()
            conn=sqlite3.connect('bookshop.db')
            c = conn.cursor()
            c.execute("SELECT * from Employees WHERE id=? and password=?",[Userid,password])
            employeelist=c.fetchall()
            conn.commit()
            emp=None
            if not len(employeelist):
                r= messagebox.showerror("Error", "Invlaid LoginDetails")
                if r=="ok":
                    logout(master)
            emp=employeelist[0]
            global employee
            employee=Employee(emp[1],emp[2],emp[3],emp[0])

            my_label1 = Label(master, text="Update the database:", font=("Helvetica", 10), width=20, height=2)
            my_label1.grid(row=0, column=2)

            my_label1 = Label(master, text="", font=("Helvetica", 10), width=20, height=2,bg="bisque2")
            my_label1.grid(row=0, column=0)
            logoutbut = Button(master, width=10, height=2, text="Logout",
                                 command=lambda: logout(master))
            logoutbut.grid(row=0,column=0)

            my_label1 = Label(master, text="ISBN:", font=("Helvetica", 10), width=20, height=2)
            my_label1.grid(row=1, column=1)

            isbntext = Text(master, height=1)
            isbntext.grid(row=1, column=2)

            def update( master):
                isbn_ = isbntext.get("1.0", END)
                isbn_ = isbn_.replace('\n', '')
                c.execute("SELECT  * FROM books WHERE ISBN=?",[isbn_])
                book_=c.fetchall()
                conn.commit()


                if len(book_)!=0:
                    my_label1 = Label(master, text="Note: enter no of books to be deleted in negative", font=("Helvetica", 10),height=2,bg="bisque2")
                    my_label1.grid(row=2, column=2)
                    my_label1 = Label(master, text="No of books to be added or deleted:", font=("Helvetica", 10), height=2)
                    my_label1.grid(row=3, column=1)
                    add_books = Text(master, height=1)
                    add_books.grid(row=3, column=2)
                    def butsave(master,book):
                        copies_=add_books.get(1.0,END)
                        copies_ = copies_.replace('\n', '')
                        print(copies_,1)
                        book=Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8])
                        BookDB().add_book(book,copies_)
                        r=messagebox.showinfo("Update","Update complete")
                        if r=="ok":
                            logout(master)


                    butforsave=Button(master, text="Save changes", font=("Helvetica", 10),
                                           width=20, height=1, bg='green',
                                           command=lambda: butsave( master,book_[0]))
                    butforsave.grid(row=4, column=2)
                    '''my_label1 = Label(self.master, text="Change the price:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=3, column=1)
                    add_books = Text(self.master, height=1)
                    add_books.grid(row=3, column=2)
                    my_label1 = Label(self.master, text="Change rack number", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=3, column=1)
                    add_books = Text(self.master, height=1)
                    add_books.grid(row=3, column=2)'''

                else:
                    my_label1 = Label(master, text="Please fill up the details:", font=("Helvetica", 10), width=20,
                                      height=2)
                    my_label1.grid(row=2, column=2)

                    my_label1 = Label(master, text="Book Title:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=3, column=1)

                    BookTitletext = Text(master, height=1)
                    BookTitletext.grid(row=3, column=2)

                    my_label1 = Label(master, text="Author:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=4, column=1)

                    Authortext = Text(master, height=1)
                    Authortext.grid(row=4, column=2)

                    my_label1 = Label(master, text="Publisher name:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=5, column=1)

                    Publishertext = Text(master, height=1)
                    Publishertext.grid(row=5, column=2)

                    my_label1 = Label(master, text="Price:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=6, column=1)

                    Pricetext = Text(master, height=1)
                    Pricetext.grid(row=6, column=2)

                    my_label1 = Label(master, text="Rack No:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=7, column=1)

                    Racktext = Text(master, height=1)
                    Racktext.grid(row=7, column=2)

                    my_label1 = Label(master, text="No of Copies to be added:", font=("Helvetica", 10), width=20,
                                      height=2)
                    my_label1.grid(row=8, column=1)

                    copiestext = Text(master, height=1)
                    copiestext.grid(row=8, column=2)

                    my_label1 = Label(master, text="Threshold:", font=("Helvetica", 10), width=20, height=2)
                    my_label1.grid(row=9, column=1)

                    Thresholdtext = Text(master, height=1)
                    Thresholdtext.grid(row=9, column=2)

                    my_label1 = Label(master, text="Avererage Procurment Time:", font=("Helvetica", 10), width=20,
                                      height=2)
                    my_label1.grid(row=10, column=1)

                    Averagetext = Text(master, height=1)
                    Averagetext.grid(row=10, column=2)

                    def save(master, isbn_):
                        #self.master = master
                        global BookTitle_
                        BookTitle_ = BookTitletext.get(1.0, END)
                        BookTitle_ = BookTitle_.replace('\n', '')
                        global Author_
                        Author_ = Authortext.get(1.0, END)
                        Author_ = Author_.replace('\n', '')
                        global publishername
                        publishername = Publishertext.get(1.0, END)
                        publishername = publishername.replace('\n', '')
                        global Price_
                        Price_ = Pricetext.get(1.0, END)
                        Price_ = Price_.replace('\n', '')
                        global Rack_
                        Rack_ = Racktext.get(1.0, END)
                        Rack_ = Rack_.replace('\n', '')
                        global copies_
                        copies_ = copiestext.get(1.0, END)
                        copies_ = copies_.replace('\n', '')
                        global Threshold_
                        Threshold_ = Thresholdtext.get(1.0, END)
                        Threshold_ = Threshold_.replace('\n', '')
                        global Average_
                        Average_ = Averagetext.get(1.0, END)
                        Average_ = Average_.replace('\n', '')
                        #,bookTitle = '',authorName = '',price =0,ISBN =0,noOfCopies =0,rackNo =0,noOfRequests =1,averageDays =0,threshold = 0
                        book=Book(BookTitle_,Author_,Price_,isbn_,copies_,Rack_,1,Average_,Threshold_)
                        BookDB().add_book(book,copies_)

                        conn=sqlite3.connect('bookshop.db')
                        c = conn.cursor()
                        c.execute("SELECT rowid, * FROM Publishers WHERE publisherName=?",[publishername])
                        publishers_=c.fetchall()
                        conn.commit()

                        if not len(publishers_):
                            for item in master.winfo_children():
                                item.destroy()
                            # check if publisgher is registerd
                            my_label1 = Label(master, text="Update the database:", font=("Helvetica", 10), width=20, height=2)
                            my_label1.grid(row=0, column=2)
                            logoutbut = Button(master, width=10, height=2, text="Logout",
                                                 command=lambda: logout(master))
                            logoutbut.grid(row=0,column=0)
                            messagebox.showinfo("Publisher is not registered", "register the publisher")
                            my_label1 = Label(master, text="Please fill up the details:", font=("Helvetica", 10),
                                              width=20, height=2)
                            my_label1.grid(row=2, column=2)

                            my_label1 = Label(master, text="Publisher name:", font=("Helvetica", 10), width=20,
                                              height=2)
                            my_label1.grid(row=3, column=1)

                            Publishername = Text(master, height=1)
                            Publishername.grid(row=3, column=2)
                            #publishername.insert(1.0,publishers_)

                            my_label1 = Label(master, text="Vendor name:", font=("Helvetica", 10), width=20, height=2)
                            my_label1.grid(row=4, column=1)

                            Vendorname = Text(master, height=1)
                            Vendorname.grid(row=4, column=2)

                            def savePub( master, publishername):
                                global Vendor_
                                Vendor_ = Vendorname.get(1.0, END)
                                Vendor_ = Vendor_.replace('\n', '')

                                c.execute("SELECT * FROM Vendors WHERE vendorName=?",[Vendor_])
                                vendors_=c.fetchall()
                                conn.commit()
                                r=None
                                if not len(vendors_):
                                    for item in master.winfo_children():
                                        item.destroy()
                                    # check if publisgher is registerd
                                    my_label1 = Label(master, text="Update the database:", font=("Helvetica", 10), width=20, height=2)
                                    my_label1.grid(row=0, column=2)
                                    logoutbut = Button(master, width=10, height=2, text="Logout",
                                                         command=lambda: logout(master))
                                    logoutbut.grid(row=0,column=0)
                                    messagebox.showinfo("Vendor is not registered", "register the Vendor")
                                    my_label1 = Label(master, text="Please fill up the details:",
                                                      font=("Helvetica", 10), width=20, height=2)
                                    my_label1.grid(row=2, column=2)

                                    my_label1 = Label(master, text="vendor name:", font=("Helvetica", 10), width=20,
                                                      height=2)
                                    my_label1.grid(row=3, column=1)

                                    vendorname = Text(master, height=1)
                                    vendorname.grid(row=3, column=2)
                                    vendorname.insert(1.0, Vendor_)

                                    my_label1 = Label(master, text="vendorAddress :", font=("Helvetica", 10), width=20,
                                                      height=2)
                                    my_label1.grid(row=4, column=1)

                                    VendorAdd = Text(master, height=1)
                                    VendorAdd.grid(row=4, column=2)

                                    my_label1 = Label(master, text="vendor mail :", font=("Helvetica", 10), width=20,
                                                      height=2)
                                    my_label1.grid(row=5, column=1)

                                    VendorMail = Text(master, height=1)
                                    VendorMail.grid(row=5, column=2)

                                    def saveven( master, publishername):

                                        global vendor_name
                                        vendor_name = vendorname.get(1.0, END)
                                        vendor_name = vendor_name.replace('\n', '')
                                        global vendor_add
                                        vendor_add = VendorAdd.get(1.0, END)
                                        vendor_add = vendor_add.replace('\n', '')
                                        global vendor_mail
                                        vendor_mail = VendorMail.get(1.0, END)
                                        vendor_mail = vendor_mail.replace('\n', '')

                                        Vendor_=Vendor(None,vendor_name,vendor_add,vendor_mail)
                                        VendorDB().add_vendor(Vendor_)
                                        c.execute("SELECT * FROM Vendors WHERE vendorName=?",[Vendor_.get_name()])
                                        vendors_=c.fetchall()
                                        conn.commit()
                                        publisher_=Publisher(None,publishername,vendors_[0][0])
                                        PublisherDB().add_publisher(publisher_)
                                        r =messagebox.showinfo("Added", "Publisher Vendor and Book added")
                                        if r=="ok":
                                            logout(master)



                                    savevenbutton = Button(master, text="Save Publisher", font=("Helvetica", 10),
                                                           width=20, height=1, bg='green',
                                                           command=lambda: saveven( master, publishername))
                                    savevenbutton.grid(row=10, column=2)

                                else:
                                    r = messagebox.showinfo("Added", "publisher and book added")
                                    vendor_=vendors_[0]
                                    publisher_=Publisher(None,publishername,vendor_[0])
                                    PublisherDB().add_publisher(publisher_)
                                    if(r=="ok"):
                                        logout(master)

                            savePubbutton = Button(self.master, text="Save Publisher", font=("Helvetica", 10), width=20,
                                                   height=1, bg='green',
                                                   command=lambda: savePub(master, publishername))
                            savePubbutton.grid(row=10, column=2)
                        else:
                            r = messagebox.showinfo("Added", "Book added")
                            if r == "ok":
                                logout(self.master)

                    savebutton = Button(self.master, text="Save changes", font=("Helvetica", 10), width=20, height=1,
                                        bg='green', command=lambda: save(master, isbn_))
                    savebutton.grid(row=11, column=2)

            findbutton = Button(self.master, text="Find", font=("Helvetica", 10), width=20, height=1, bg='green',
                                command=lambda: update(master))
            findbutton.grid(row=1, column=3)

        loginButton = Button(self.master, text="Login", font=("Helvetica", 10), width=20, height=2, bg='green',
                             command=lambda: login(self.master))
        loginButton.place(relx=0.5, rely=0.4, anchor=CENTER)




root = Tk()
mainnotebook = ttk.Notebook(root)
mainnotebook.grid(row=0, column=0, columnspan=3)
customertab = Frame(mainnotebook, width=1000, height=1000, bg="bisque2")
customertab.grid(row=0, column=0, columnspan=3)
mainwindow = CustomerFrame(customertab)
mainnotebook.add(customertab, text="Customer")
employeetab =Frame(mainnotebook,bg="bisque2")
employeetab.grid(row=0, column=0, columnspan=3)
mainnotebook.add(employeetab, text="Employee")
employeeframe=EmployeeFrame(employeetab)
root.mainloop()
