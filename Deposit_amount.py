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
