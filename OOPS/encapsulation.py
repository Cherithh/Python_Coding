class Bank:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,deposit):
        self.__balance += deposit

    def show_balance(self):
        print("Balance:",self.__balance)


b = Bank(5000)
b.deposit(3000)
b.show_balance()
