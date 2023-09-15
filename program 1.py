#program to display the banking process like deposit,withdrawal,checking balance 
class BankAccount:

  def __init__(self, account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Amount Deposited ₹{}. New balance: ₹{}".format(amount,
                                                            self.__account_balance))
    else:
      print("Invalid Deposit Ammount.")

   
  def withdrawl(self,amount):
   if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
     print("withdrawl ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
   else:
     print("Invalid withdrawal amount or insufficient balance.")

  
  def display_balance(self):
   print("Account balance for {} (Account No #{}): balance ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


account = BankAccount(account_number="Ac12345", 
                      account_holder_name="Anuppriya",
                      initial_balance=50000.0)
account.display_balance()
account.deposit(5000.0)
account.withdrawl(25000.0)
