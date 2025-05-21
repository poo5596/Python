#conditional statement

#1.if-else

n=int(input("enter the number :- "))
if(n%2==0):
    print("even number")
else :
    print("odd number")

#2.voting program

age=int(input("enter the age:- "))
if(age>=18):
        print("eligible for voting")
else:
        print("not eligible for voting")

#3.name program

name=input("enter the name :- ")
if(name=="pooja"):
     print("name is correct ")
else:
    print("name is wrong ")


#4.if-elif-else

n=int(input("enter a number :- "))
if(n>10 and n<20):
      print("range is 10-20")
elif(n>20 and n<100):
    print("range is 20-100")
else:
    print("not in range")



#5.grade multiple elif condition 

result=int(input("enter the result:-"))
if(result>=35 and result<=40):
    print("B Grade")

elif(result>=40 and result<=100):
    print("A Grade")

elif(result>100):
    print("invalid grade")

else:
    print("Fail")

#6.operator program

operator=(input("enter the operator :- "))
if(operator=="+" or operator=="-"):
    print("arithematic operator")

elif(operator=="="):
    print("assigment operator")

else:
    print("invalid operator")

#if, if-else , if-else-if-else (multiple if-else),
#if-elif-elif-else(multiple elif), nested if


n1= int(input(" enter the number :"))
n2= float(input(" enter the number :"))

if (n1>n2):
    print("greater")
else :
    print("small")

if (n1==n2):
    print("equal num")
else:
    print("not equal")


if(n1==n2):
    print("outer loop")
    if(n1==10):
        print("inner loop")
    else :
        print("inner loop not executed")
else :
    print("outer loop not executed")
    


    
            
            
      
