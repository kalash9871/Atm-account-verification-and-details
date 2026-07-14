#ATM account Verificatioin through authentic username and password
username="kalash"
password="1234"

n=input("Enter ur username :- ")
if username==n:
    p=input("Enter your password:- ")
    if password==p:
        print("correct Password! U Successfully entered in your Acoount Details")
    
        #Account
        Balance_amount=5000
        while True:
            print("\n---Account---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                Deposit=int(input("Enter your amount:- "))
                result=Balance_amount+Deposit
                print(result)
            elif choice==2:
                Withdraw=int(input("Enter the u want to withdraw:- "))
                if Balance_amount>=Withdraw:
                    r=Balance_amount-Withdraw
                    print(r)
                else:
                    print("Insufficient Amount")
            elif choice==3:
                print("Your Balance Amount is :- ",Balance_amount)
            elif choice==4:
                print("Exit! THANKS FOR VISIT!")
                break
            else:
                print("invalid choice")
    else:
        print("incorrect password!")
else:
    print("Incorrect username")