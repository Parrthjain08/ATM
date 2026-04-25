def Statement():
    print("Account Statement:")
    if money_withdraw > 0 or money_deposit > 0:
        print(f"You withdrew {money_withdraw:.2f}")
        print(f"You deposited {money_deposit:.2f}")
    print(f"Your current balance is {Total_money:.2f}")
    print("transcation records")
