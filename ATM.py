from Enter_pin import pin
from Withdraw_amount import Withdraw
from Deposit_amount import Deposit
from Account_statement import Statement
from Check_balance import Chcek_balance
def Atm():
    pin()
    while True:
        print("\nPlease select an option:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            Withdraw()
        elif choice == '2':
            Deposit()
        elif choice == '3':
            Check_balance()
        elif choice == '4':
            Statement()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

Atm()
