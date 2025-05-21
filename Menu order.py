idly=45
dosa=70
masaladosa=80
meduvada=55
pongal=80
sambar=25

bill=0

print("Menu")
print("1.idly-Rs.45")
print("2.dosa-Rs.70")
print("3.masaladosa-Rs.80")
print("4.meduvada-Rs.55")
print("5.pongal-Rs.80")
print("6.sambar-Rs.25")

while True:
    choice=int(input("enter your choice(1-6):\n:"))
    if choice<1 or choice>6:
        print("Invalid choice. Please select a number from 1 to 6.")
        continue

    quantity=int(input("enter the quantity(1-10):\n"))
    if quantity<=0 or quantity>10:
        print("Invalid quantity. Please enter a number from 1 to 10.")
        continue

    if choice==1:
        bill+=idly*quantity
    elif choice==2:
        bill+=dosa*quantity
    elif choice==3:
        bill+=masaladosa*quantity
    elif choice==4:
        bill+=meduvada*quantity
    elif choice==5:
        bill+=pongal*quantity
    elif choice==6:
        bill+=sambar*quantity

    choice_2=int(input("do you want to continue ordering?(1 for yes/0 for no:)\n"))
    if choice_2==1:
        continue
    else:
        print("your total bill is Rs."+str(bill))
        break


