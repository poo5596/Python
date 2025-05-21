Balance=1000
pin=1234
while True:
    print("1.Balance")
    print("2.Withdrwal")


    choice=int(input("enter your choice"))
    if choice==1:
        print("your balance is:",Balance)
    elif choice==2:
        upin=int(input("enter your pin"))
        if upin==pin:
            continue
        elif upin!=pin:
            print("invalid pin")
            for i in upin:
                if i==3:
                    break
                print("lock")
                    
           
                
            '''
           while upin<=1:
           
                print("invalid pin")
                upin+=1
                if upin==3:
                    break
                    print("your pin lock")
                    
                '''
        
