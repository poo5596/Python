paneer_kolhapuri=300
chapti=10
dal=140
jeeraRice=120
VegMixShabji=280

total_bill=0

print("Welcome to Hotel Priyanka")
print("Our Menu")
print("1.paneer_kolhapuri-Rs.300")
print("2.chapti-Rs.10")
print("3.dal-Rs.140")
print("4.jeeraRice-Rs.120")
print("5.VegMixShabji-Rs.280")

def bill(price,quantity):
    global total_bill
    total_bill+=price*quantity
    print(total_bill)

def Total_bill():
    print(f"Your Total bill is Rs.{total_bill}")

while True:
    choice=int(input("enter your choice between (1-5)"))
    if choice<1 or choice>5:
        print("invalid choice. Please choice between (1-5)")
        continue
    quantity=int(input("enter the quantity(1-above):\n"))
    if quantity<=0:
        print("Invalid quantity. Please enter at least 1 quantity")

    if choice==1:
        bill(paneer_kolhapuri,quantity)
    elif choice==2:
        bill(chapti,quantity)
    elif choice==3:
        bill(dal,quantity)
    elif choice==4:
        bill(jeeraRice,quantity)
    elif choice==5:
        bill(VegMixShabji,quantity)

    choice_2=int(input("do you want to continue your ordering?(1 for yes / 0 for no)\n"))
    if choice_2==1:
        continue
    else:
        Total_bill()
        break
    
