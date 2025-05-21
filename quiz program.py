print("Quiz Game")

score=0

print("1.What is the Date of Independent day")
print("2.What is the Biggest river of India")
print("3.Name of First Prime Mishter of India")
print("4.What is the full form of WHO")
print("5. score")

while True:
    choice=int(input("enter your choice"))
    if choice<0 or choice>5:
        print("Invlid Choice")

    if choice==1:
        Ans=int(input("enter your day in number "))
        if Ans==15:
            print("Right Ans")
            score+=1
        else:
            print("Wrong Ans, correct ans is 15")
    elif choice==2:
        Ans=input("enter river name")
        if Ans=="Ganga" or Ans=="ganga":
            print("Right Ans")
            score+=1
        else:
            print("Wrong Ans,correct ans is Ganga")
    elif choice==3:
        Ans=input("enter First prime Mishter of india's name")
        if Ans=="Jawaharlal Nehru" or Ans=="jawaharlal Nehru" or Ans=="Jewaharlal Nehru" or Ans=="jawaharlal nehru" or Ans=="JAWAHARLAL NEHRU":
            print("Right Ans")
            score+=1
        else:
            print("Wrong Ans, correct ans is Jawaharlal Nehru")
    elif choice==4:
        Ans=input("Enter Full form of WHO")
        if Ans=="World Health Organisation" or Ans=="world health organisation" or Ans=="WORLD HEALTH ORGANISATION":
            print("Right Ans")
            score+=1
        else:
            print("Wrong Ans, correct ans is World Health Organisation")
    elif choice==5:
        print("Your Total Score is out of 4/",+score)


    
        
    





