def pin():
        user_pin = input("Enter your 4 digit pin: ")   
        if user_pin=="0000" or  user_pin=="10000":
            print("Invalid pin. Access denied.")
            return
        print("Pin accepted")
