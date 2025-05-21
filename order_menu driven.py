#Price of item

Idly=20
Dosa=30
Masala_Dosa=40
Medu_Vada=20
Chese_Masala_Dosa=60

bill=0
total=0

while True:
    print("1.Idly\n2.Dosa\n3.Masala Dosa\n4.Medu Vada\n5.Pongal\n6.Chese Masala Dosa")
    choice=int(input("enter your order:"))

    if choice==1: 
        Idly_plat_quantity=int(input("Idly_plat_quantity:"))
        choice=int(input("do you want to continue for more order(1 for yes / 0 for no)"))
        if choice==1:
              continue
        else:
            print("bill of Idly:",Idly*Idly_plat_quantity)
            break
    if choice==2:
        Dosa_plat_quantity=int(input("Dosa_plat_quantity:"))
        choice=int(input("do you want to continue for more order(1 for yes / 0 for no)"))
        if choice==1:
              continue
        else:
            print("bill of dosa:",Dosa*Dosa_plat_quantity)
            break
    if choice==3:
        Masala_Dosa_plat_quantity=int(input("Dosa_plat_quantity:"))
        choice=int(input("do you want to continue for more order(1 for yes / 0 for no)"))
        if choice==1:
              continue
        else:
            print("bill of dosa:",Dosa*Dosa_plat_quantity)
            break

    
   
    
        
