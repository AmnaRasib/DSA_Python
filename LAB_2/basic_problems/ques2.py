# Encapsulation with Getters and Setters
class BankAccount:
    # Account Number
    def setAccountNo (self,accountNo):
         self.__accountNo=accountNo
    def getAccountNo (self,accountNo):
         return self.__accountNo
     # balance
    def setbalance (self,balance):
         self.__balance=balance
    def getbalance (self,balance):
         return self.__balance
b=BankAccount()
print("Account Number: ",b.setAccountNo(12345),b.getAccountNo())
print("Balance: ",b.setbalance(1000),b.getbalance())

    