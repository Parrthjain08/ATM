global Total_money
Total_money = float(input("Enter the amount in your account: "))
global money_deposit
global money_withdraw
money_deposit = 0.0
money_withdraw = 0.0
# check balance
def Check_balance():
    print(f"Your current balance is {Total_money:.2f}")

def pin():
        user_pin = input("Enter your 4 digit pin: ")   
        if user_pin=="0000" or  user_pin=="10000":
            print("Invalid pin. Access denied.")
            return
        print("Pin accepted")
# deposit
def Deposit():
    global Total_money
    global money_deposit
    money_deposit = float(input("Enter the amount to deposit: "))
    if money_deposit > 0:
        print(f"You have deposited {money_deposit:.2f}")
        Total_money = Total_money + money_deposit
        print(f"Your new balance is {Total_money:.2f}")
    else:
        print("Invalid amount. Please enter a positive value.")

# withdrawal
def Withdraw():
    global Total_money
    global money_withdraw
    money_withdraw = float(input("Enter the amount to withdraw: "))
    if Total_money >= money_withdraw and money_withdraw > 0:
        print(f"You have withdrawn {money_withdraw:.2f}")
        Total_money = Total_money - money_withdraw
        print(f"Your new balance is {Total_money:.2f}")
    else:
        print("Invalid amount. Please enter a positive value.")

def Statement():
    print("Account Statement:")
    if money_withdraw > 0 or money_deposit > 0:
        print(f"You withdrew {money_withdraw:.2f}")
        print(f"You deposited {money_deposit:.2f}")
    print(f"Your current balance is {Total_money:.2f}")
    print("transcation records")
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
