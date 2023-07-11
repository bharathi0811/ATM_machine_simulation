class InsufficientFundsException(Exception):
    pass
class InvalidAmountException(Exception):
    pass

class ATM:
    def __init__(self,initial_balance =0):
        self.balance = initial_balance
    def deposit(self,amount):
        if amount<=0:
            raise InvalidAmountException("Invalid amount. Please enter a positive number")
        self.balance+=amount
        print(f"Deposited Amount: {amount}. \nYour new balance is {self.balance}")
    def withdraw(self,amount):
        if amount<=0:
            raise InvalidAmountException("Invalid amount. Please enter a positive number")
        elif amount>self.balance:
            raise InsufficientFundsException("Cannot Withdraw more than Balance amount")
        self.balance-=amount
        print(f"Withdraw amount:{amount}.\nNew Balance :{self.balance}")
    def display_balance(self):
        print(f"Current Balance:{self.balance}")

def atm_machine():
    atm=ATM(1000)
    while True:
        print("             ATM MENU             ")
        print("1.Deposit Funds")
        print("2.Withdraw Amount")
        print("3.Current Balance")
        print("4.EXIT")

        n = input("Enter your Choice(1-4):")
        if n == "1":
            try:
                amount1 = float(input("Enter the amount to deposit:"))

                atm.deposit(amount1)
            except ValueError:
                print("Enter the valid Amount")
            except InvalidAmountException as err:
                print(err)
        elif n == "2":
            try:
                amount2 = float(input("Enter the amount to withdraw:"))
                atm.withdraw(amount2)
            except ValueError:
                print("Enter the valid amount")
            except InsufficientFundsException as err:
                print(err)
        elif n == "3":
            atm.display_balance()
        elif n == "4":
            print("Thank you for using our ATM.")
            break
        else:
            print("Invalid choice . choose between 1-4")


atm_machine()


























