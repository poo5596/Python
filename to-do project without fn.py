print("To-Do-List Menu:")
print("1. Add a task")
print("2. View tasks")
print("3. Remove tasks")
print("4.Quit")

list=[]

while True:
    choice=int(input("enter your choice between (1-4)"))
    if choice<0 or choice>4:
        print("Invalid To-Do Menu")

    if choice==1:
        
        task=(input("enter your task : "))
        list.append(task)
        print("Task Added Succesfully")
        

    elif choice==2:
        print(list)

    elif choice==3:
        remove=int(input("enter remove index number"))
        
        list.pop(remove)
        print(list)
    elif choice==4:
        choice=int(input("do you want Quit or continue (1 for continue / 0 for Quit"))
        if choice==1:
            continue;
        else:
            
            print("Quit")
            break;

    
        
        
        
    

