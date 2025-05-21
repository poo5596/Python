idly=50
dosa=70
meduvada=50
sambar=20

total_bill=0

print("menu")
print("1.idly-Rs.50")
print("2.dosa-Rs.70")
print("3.meduvada-Rs.50")
print("4.sambar-Rs.20")

def add_to_bill(price,quantity):
    global total_bill
    total_bill+=price*quantity
    print(total_bill)

def print_total_bill():
    print(f"Your total bill is Rs.{total_bill}")
        
while True:
    choice=int(input("enter your choice(1-6):\n:"))
    if choice<1 and choice>6:
        print("Invalid choice. Please select a number from 1 to 6.")
        continue

    quantity=int(input("enter the quantity(1-10):\n"))
    if quantity<=0 or quantity>10:
        print("Invalid quantity. please enter a number from 1 to 10.")
        continue

    if choice==1:
        add_to_bill(idly,quantity)
   
    elif choice==2:
        add_to_bill(dosa,quantity)
       
    elif choice==3:
        add_to_bill(meduvada,quantity)
        
    elif choice==4:
        add_to_bill(sambar,quantity)
      
        
    choose=int(input("do you want to continue ordering? (1 for yes/0 for no:)\n"))
    if choose==1:
        continue
    else:
       print_total_bill()
       break

