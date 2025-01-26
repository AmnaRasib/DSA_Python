#  Encapsulation Using Private Members
class BankAccount:
    def __init__(self, accountNo,balance):
        self.__acountNo= accountNo
        self.__balance= balance
        # deposit money
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited Amount: {amount} ")
        #withdraw cash
    def withdraw(self,amount):
        if amount<= self.__balance:
           self.__balance-=amount
           print(f"Withdraw Amount: {amount} ")
        else:
            print("Insufficient funds")

    def display_Balance(self):
        print(f"Account Number: {self.__acountNo} \n Current Balance: {self.__balance}")

account =BankAccount("12345678",1000)
account.deposit(500)
account.withdraw(700)
account.display_Balance()
    
    