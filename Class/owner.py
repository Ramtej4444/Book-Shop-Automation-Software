from Class import Employee
from DataBaseClass import BookDB


class Owner(Employee):
    def __init__(self):
        super().__init__()
        self.empCode = 3

    # display all books which have fallen below a threshold value
    def viewThreshold(self):
        booklist = BookDB().get_booksbelowthreshold()
        totalout =""
        for item in booklist:
            totalout = totalout + "\nBook Title:"+str(item.get_booktitle())+"\n" + "ISBN:"+str(item.get_isbn())+"\n"+"No of Copies:" + str(item.get_noofcopies())+"\n"
        return totalout
