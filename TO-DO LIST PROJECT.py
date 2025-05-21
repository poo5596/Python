task1=[]

def Add_a_task(task1):
    task=(input("enter your task :"))
    task1.append(task)
    print("Task Added successfully")
    
def View_tasks(task1):
    
    print("Tasks:",task1)

def remove_a_task(task1):
    View_tasks(task1)
    remove=int(input("enter Index number you wants to remove: "))
    task1.pop(remove)
    print("Removed in list succesfully")
    



while True:
    print("To-Do List Menu:")
    print("1.Add A task")
    print("2.View task")
    print("3.Remove a task")
    print("4.Quit")

    
    
    choice=int(input("enter your choice"))
    if choice==1:
        Add_a_task(task1)
    elif choice==2:
        View_tasks(task1)
    elif choice==3:
        remove_a_task(task1)
    elif choice==4:
        choice1=int(input("Do you Really wants to continue click 1 for yes / and 0 for no : "))
        if choice1==1:
            continue;
        else:
            print("Exit")
            break;

        
        
