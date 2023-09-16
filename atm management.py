Username = "Krishna"
password = 123
amount = 25000

print("welcome to the ATM")

Name = input("please enter your Username: \n")
Password =  int(input("please enter your password: \n"))

if Name == Username and password == Password:
    print("""
    1.Balance Enquiry
    2.Withdraw
    3.Deposit
    4.Mini Statement
    5.exit
    """)
    
    option = int(input("Select your option: \n"))

    if option == 1:
        print("Your current Balance: ",amount )
    elif option == 2:
        wit = int(input("Enter amount: \n"))
        amount -= wit
        print("Your current Balance: ",amount)
    elif option == 3:
        dep = int(input("Enter amount: \n"))
        amount += dep
        print("Your current Balance: ",amount)
    elif option == 4:
        print("*********ATM***********")
        print("Username: ",Username)
        print("Total Amount: ",amount)
        print("Thanks For Visiting")
        print("***********************")
    elif option ==5:
        exit()
else:
    print("please enter correct 'username' or 'password' ")

    
    

    