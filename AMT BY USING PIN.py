def pin():
    global pin
    if upin==pin:
        continue
    elif upin!=pin:
        print("invalid pin, Try again!!!")
        upin=int(input("enter your pin"))
        if upin==pin:
            
            continue
        elif upin!=pin:
            print("invalid pin,Try gain!!!")
            upin=int(input("enter your pin"))
            if upin!=pin:
                continue
            elif upin!=pin:
                print("your card has blocked for 24 hr ")

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
        pin()
        break
                    
            
            
      
            
            
            
            

            
            
            
            

