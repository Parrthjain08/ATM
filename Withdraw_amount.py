from Variables_used import total_money,money_withdraw
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
