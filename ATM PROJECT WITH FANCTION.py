

balance=0

def YourBalance():
    print("your balance is :-",balance)


def Withdrwal():
    global balance
    if amount<=balance:
        balance-=amount
        print("your withdrwal is scussfull")
    else:
        print("insifient Balance,Try Again!!")
    
    print("your balance is :-",balance)

def Deposit():
    global balance
    balance+=amount
    print("your balance is :-",balance)

while True:
    #main Programm
    print("ATM Project\n")
    print("1.Balance\n")
    print("2.Withdrwal\n")
    print("3.Deposit\n")
    print("4.exit\n")
    choice=int(input("enter your choice(1-4)"))

    
    if choice==1:
        YourBalance()
    elif choice==2:
        amount=int(input("enter your amount"))
        Withdrwal()
    elif choice==3:
        amount=int(input("enter your amount"))
        Deposit()
    elif choice==4:
        choice=int(input("Do you want to exit 1 for yes / 0 for no"))
        if choice==1:
            print("exit")
            break
        else:
            continue

        
    
    
