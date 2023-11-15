import random
pin_code = random.randint(1000,9999)
user_pin = int(input("Please enter you 4 digits\n"))
if len(str(user_pin)) != 4 : 
    print("Please entre 4 digits")
elif user_pin == pin_code : 
    print("Succed!")
else : 
    print("Not matched!")
    print(f"PIN computer is : {pin_code}")
