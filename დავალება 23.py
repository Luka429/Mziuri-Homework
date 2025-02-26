class Bank_Account:
    def __init__(self,account_name,balance):
        self.__account_name = account_name
        self.__balance = balance

    def get_account_name(self):
        return self.__account_name

    def set_account_name(self,setter):
        self.__account_name = setter

    def deposit(self,deposit_amount):
        deposit_amount = float(deposit_amount)
        self.__balance = self.__balance + deposit_amount
        return f"The deposit was successful,your balance is {self.__balance}"

    def withdraw(self,withdraw_amount):
        withdraw_amount = float(withdraw_amount)
        if self.__balance > withdraw_amount:
            self.__balance -= withdraw_amount
            return f"The withdraw was successful,your balance is {self.__balance}"
        else:
            return f"The balance isn't enough,its over by: {withdraw_amount - self.__balance}"

bank1 = Bank_Account(input("Enter your account name: "),float(input("Enter your balance: ")))
action = int(input("Enter 1 for deposit,2 for withdraw: "))

if action == 1:
    print(bank1.deposit(input("Enter the deposit amount: ")))
elif action == 2:
    print(bank1.withdraw(input("Enter the withdraw amount: ")))
else:
    print("Pleas enter the options provided (1/2)")







