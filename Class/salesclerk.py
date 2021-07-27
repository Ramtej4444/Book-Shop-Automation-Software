from Class import Employee
from Class import Transaction
from DataBaseClass import TransactionDB


class SalesClerk(Employee):
    def __init__(self):
        super().__init__(self)
        self.empCode = 1

    def complete_transaction(self, dateOfTransaction, bookISBN, noOfCopies, name, mobilenumber):
        # transactionId,dateOfTransaction,bookISBN,noOfCopies,name,mobilenumber.
        transaction_ = Transaction(None, dateOfTransaction, bookISBN, noOfCopies, name, mobilenumber)
        TransactionDB().add_transaction(transaction_)
