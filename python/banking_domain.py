
class Bank:

    # Fudging an 11 digit IFSC CODE with incr branch number
    # First 4 digits are from bank name a zero for future use
    # and last 6 are a branch id
    IFSC_BRANCH_CODE = 0 
    IFSC_DEFAULT_BANK_NAME = "DEFN"

    def __init__(self, bank_name="Default Bank", branch_name="Default Branch",\
                 location="Lake Tahoe" ):

        self.bankname = bank_name
        self.branchname = branch_name
        self.loc = location

        if len(bank_name) >= 4:
            self.IFSC_Code = bank_name[0:4].upper() +\
                             "0%06d" % Bank.IFSC_BRANCH_CODE
        else:
            self.IFSC_Code = Bank.IFSC_DEFAULT_BANK_NAME +\
                             "0%06d" % Bank.IFSC_BRANCH_CODE

        Bank.IFSC_BRANCH_CODE += 1 
        if Bank.IFSC_BRANCH_CODE > 999999:
            Bank.IFSC_BRANCH_CODE = 0

   
class Customer:

    CUSTOMER_ID = 0

    def __init__(self, cust_name="Joe", addr="1455 fischer st\nReno NV, 97349",\
                 contact_details="email:j@gmail.com,phone:32-321-0099" ):

        self.custname = cust_name
        self.address = addr
        self.contactdetails = contact_details
        self.CustomerID = Customer.CUSTOMER_ID
        Customer.CUSTOMER_ID += 1
       

class Account(Bank):

    ACCOUNT_ID = 0

    def __init__(self, bank_name="Default Bank", branch_name="Default Branch",\
                 location="Lake Tahoe", cust=None, bal=0 ):

        super().__init__(bank_name, branch_name, location) 
        self.Customer = cust
        self.balance = bal
        self.AccountID = Account.ACCOUNT_ID
        Account.ACCOUNT_ID += 1
   
    # Can add more here just wasn't really specified
    def getAccountInfo(self):

        info = "BANK NAME: %s\
                \nBRANCH NAME: %s\
                \nIFSC CODE: %s\
                \nLOCATION: %s\
                \nACCOUNT ID: %d\
                \nBALANCE: %0.2f$" % \
                (self.bankname, self.branchname, self.IFSC_Code,\
                 self.loc, self.AccountID, self.balance)


        if self.Customer is not None:
            info += "\nCUSTOMER: %s\
                     \nCUSTOMER ID: %d" %\
                    (self.Customer.custname, self.Customer.CustomerID)

        return info

    def deposit(self, val, attr):

       if val < 1:
           raise Exception("Invalid Deposit Ammount, Value Must Be Positive")

       self.balance += val

    def withdraw(self, val):

       if val < 1:
           raise Exception("Invalid Withdraw Ammount, Value Must Be Positive")

       self.balance -= val
      
    def getBalance(self):
       return self.balance


class SavingsAccount(Account):


    def __init__(self, bank_name="Default Bank", branch_name="Default Branch",\
                 location="Lake Tahoe", cust=None, bal=0, smin_balance=0):

       # set initial balance to smin_balance so program below can run to end
       # more for QOL than anything could also do an initial deposit check
       # but the assignment does not specify this...
       super().__init__(bank_name, branch_name, location, cust, smin_balance) 
       self.SMinBalance = smin_balance

    def getSavingsAccountInfo(self):
        return self.getAccountInfo() + "\nMINBALANCE: %.02f$" % self.SMinBalance

    # just puting these here cause the assignment says too
    # but not necessary
    def deposit(self, val, attr):

       if val < 1:
           raise Exception("Invalid Deposit Ammount, Value Must Be Positive")

       self.balance += val

    def withdraw(self, val):

       if val < 1:
           raise Exception("Invalid Withdraw Ammount, Value Must Be Positive")

       if self.balance - val < self.SMinBalance:
           raise Exception("Withdraw Exceeds Minimum Balance")

       self.balance -= val

    # just puting these here cause the assignment says too
    # but not necessary   
    def getBalance(self):
       return self.balance



class StartBank(object):

    def run(self):

        # Again can add more just not sure what specifically... 
        bankname        = input("ENTER BANK NAME: ")
        branchname      = input("ENTER BRANCH NAME: ")
        loc             = input("ENTER LOCATION: ")
        custname        = input("ENTER CUSTOMER NAME: ")
        address         = input("ENTER CUSTOMER ADDRESS: ")
        contactdetails  = input("ENTER CONTACT DETAILS: ")
        sminbalance     = input("ENTER SAVINGS MIN BALANCE: ")

        try:
            sminbalance = float(sminbalance)
        except ValueError:
            print("Invalid Minimum Balance Entered Using Default")
            sminbalance = 0
        
        customer = Customer(custname, address, contactdetails)

        savings_account = SavingsAccount(bank_name=bankname,\
                          branch_name=branchname, location=loc,\
                          cust=customer, smin_balance=sminbalance)

        print("\nStarting Customer and Account Info\n")
        print(savings_account.getSavingsAccountInfo() + "\n")

        try_deposit = True
        while(try_deposit): # loops until acceptable value is given

            deposit = input("ENTER AN AMOUNT TO DEPOSIT: ")

            try:
                deposit = float(deposit)
                savings_account.deposit(deposit, 'true')
                try_deposit = False
            except ValueError:
                print("Deposit Values Must Be Positive Floats")
            except Exception as e:
                print(str(e))

        print("\nSavings Account Balance is: %0.2f$\n" %\
               savings_account.getBalance())

        try_withdraw = True
        while(try_withdraw): # loops until acceptable value is given

            withdraw = input("ENTER AN AMOUNT TO WITHDRAW: ")

            try:
                withdraw = float(withdraw)
                savings_account.withdraw(withdraw)
                try_withdraw = False
            except ValueError:
                print("Withdraw Values Must Be Positive Floats")
            except Exception as e:
                print(str(e))

        print("\nSavings Account Balance is: %0.2f$\n" %\
               savings_account.getBalance())

        print("\nEnding Customer and Account Info\n")
        print(savings_account.getSavingsAccountInfo() + "\n")
           

        
if __name__ == '__main__':
    StartBank().run()

