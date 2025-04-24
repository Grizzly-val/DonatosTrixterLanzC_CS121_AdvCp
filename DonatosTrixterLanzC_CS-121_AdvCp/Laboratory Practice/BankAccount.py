from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance


    @abstractmethod
    def deposit(self, deposit_amount):
        pass
    
    @abstractmethod
    def withdraw(self, withraw_amount):
        pass


    @abstractmethod
    def display_account_type(self):
        pass




class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, deposit_amount):
        self._balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self._balance - withdraw_amount >= -5000:
            self._balance -= withdraw_amount

        else:
            print("Overdraft limit exceeded")

    def display_account_type(self):
        return "Current Account"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, deposit_amount):
        self._balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self._balance - withdraw_amount >= 0:
            self._balance -= withdraw_amount
        else:
            print("Insufficient Balance in your Savings Account")

    def display_account_type(self):
        return "Savings Account"




def print_account_details(acc):
    print(f"Account Number: {acc.account_number}")
    print(f"Balance: {acc.balance}")
    print(f"Type: {acc.display_account_type()}")
    print("-------------------------------------------------")

acc1 = SavingsAccount("SA123", 5200)
acc2 = CurrentAccount("CA456", 1000)
acc3 = CurrentAccount("CA212", 3300)
acc4 = SavingsAccount("SA254", 340)

acc1.withdraw(4000)
acc2.withdraw(1200)

print_account_details(acc1)
print_account_details(acc2)
print_account_details(acc3)
print_account_details(acc4)