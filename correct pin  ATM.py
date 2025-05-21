

Balance=1000
pin=1111

print("ATM project")
print("1.Balance")
print("2. Change pin")
print("3.withdrwal")

while True:

    choice=int(input("enter Your choice"))


    if choice==1:
               print("Your Balance is :",Balance)
    
    elif choice==2:
        upin=int(input("enter your pin"))
        if upin==pin:
            amount=int(input("enter your amount"))
            if amount<=Balance:
                Balance-=amount
                print(f"your amount debit from your a/c {amount}")
                print("your balance is:",Balance)
        elif upin!=pin:
            print("invalid pin, Try again")
            upin=int(input("enter your pin"))
            if upin==pin:
                amount=int(input("enter your amount"))
                if amount<=Balance:
                    Balance-=amount
                    print(f"your amount debit from your a/c {amount}")
                    print("your balance is:",Balance)
            elif upin!=pin:
                print("invalid pin, if enter again wrong pin your card has been blocked")
                upin=int(input("enter your pin"))
                if upin==pin:
                    amount=int(input("enter your amount"))
                    if amount<=Balance:
                        Balance-=amount
                        print(f"your amount debit from your a/c {amount}")
                        print("your balance is:",Balance)
                elif upin!=pin:
                    print("Invalid pin, your card has been blocked for 24hr, please contact with your nearest branch")
                    break
                    
                    


m1=int(input("enter value of m1"))
m2=int(input("enter value of m2"))
def multiple(q,r):
    print(q*r)
multiple(m1,m2)         
            
      
            
            
            
            

            
            
            
            

