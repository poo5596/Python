'''#write a program of discount based on bill

idly=20
dosa=30
meduvada=35

totalbill=0
discount_rate=0 

print("Menu")
print("1.idly Rs.20")
print("2.dosa Rs.30")
print("3.meduvada Rs.35")
print("4.exit")

    
def bill(price,quantity):
    global totalbill
    totalbill+=price*quantity
    print(totalbill)
    

def Totalbill():
    if totalbill<=40:
        discount_rate=0.00
    elif totalbill<=80:
        discount_rate=0.05
    elif totalbill<=100:
        discount_rate=0.10
    else:
        discount_rate=0.15
        
    discount_amount=totalbill*discount_rate
    Totalbill=totalbill-discount_amount
    print(Totalbill)
    
    
while True:
    choice=int(input("enter your choice between (1-3)"))
    if choice<1 or choice>3:
        print("invalid choice, Please select between (1-3)")
        continue
    quantity=float(input("enter your quantity"))
    if quantity<=0:
        print("invalid quanity. please select atleast 1 quantity")

    if choice==1:
        bill(idly,quantity)
    elif choice==2:
        bill(dosa,quantity)
    elif choice==3:
        bill(meduvada,quantity)


    
    choice1=int(input("do you want to continue or exit (1 for yes 0 for no)"))
    if choice1==1:
        continue
    else:
        Totalbill()
        break;'''

#program for discount based on item(choice)
idly=20
dosa=30
meduvada=35

totalbill=0
discount_rate=0 

print("Menu")
print("1.idly Rs.20")
print("2.dosa Rs.30")
print("3.meduvada Rs.35")
print("4.exit")
   
def bill(price,quantity):
    global totalbill
    totalbill+=price*quantity
    print(totalbill)
    
def Totalbill():
    if choice<=1:
        discount_rate=0.00
    elif choice<=2:
        discount_rate=0.05
    elif choice<=3:
        discount_rate=0.10
    
        
    discount_amount=totalbill*discount_rate
    Totalbill=totalbill-discount_amount
    print(Totalbill)
      
while True:
    choice=int(input("enter your choice between (1-3)"))
    if choice<1 or choice>3:
        print("invalid choice, Please select between (1-3)")
        continue
    quantity=float(input("enter your quantity"))
    if quantity<=0:
        print("invalid quanity. please select atleast 1 quantity")

    if choice==1:
        bill(idly,quantity)
    elif choice==2:
        bill(dosa,quantity)
    elif choice==3:
        bill(meduvada,quantity)
    
    choice1=int(input("do you want to continue or exit (1 for yes 0 for no)"))
    if choice1==1:
        continue
    else:
        Totalbill()
        break;
                
                
        
        
        
        
        
        
        
        
        
        
               
