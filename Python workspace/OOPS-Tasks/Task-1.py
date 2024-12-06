#Creating a custom insufficient balance exception class inheriting from
#Exception class
class InsuffucientBalanceException(Exception):
    pass

class BankAccount:
    #private proprty balance. So that it can't be accesses/modified 
    #from outside the class.
    __balance = 0.0
    def __init__(self, name):
        #account holder name is also kept private so that
        #it can't be modified from outside the class.
        self.__account_holder = name
    def deposit(self, amount):
        self.__balance = self.__balance+amount
    def withdraw(self, amount):
        try:
            if self.__balance>=amount:
                self.__balance = self.__balance-amount
            else:
                #raise Insufficient balance exception when withdrawl
                #amount is greater than the balance
                raise InsuffucientBalanceException
        #as the exception will be raised this excepet block will run
        except InsuffucientBalanceException:
            print("Exception: Insufficient Balance!!")
    def get_balance(self):
        return self.__balance

#creating a BankAccount object for Ramesh
account1 = BankAccount('Ramesh')
print(account1.get_balance())
account1.deposit(2000)
print(account1.get_balance())
account1.withdraw(1200)
print(account1.get_balance())
#trying to withdraw more amount than balance
account1.withdraw(1500)

#trying to access balance outside the class:
#In both the cases we get Attribute Error
# print(account1.balance)
# print(account1.__balance)
