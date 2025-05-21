'''n=7
fact=1
for i in range (1,n+1):
    fact=fact*i
print(fact)


n=int(input("enter your number"))
fact=1

for w in range(1,n+1):
    fact=fact*w
print(fact)

#always take fact value as 1
'''

#prime number

prime_no=[]
n=8
for i in range(1,9):
    if i==2:
        prime_no.append(i)
        print(i,"it is only even prime number")
    elif i%2==0:
        print(i,"it is not prime number")
    else:
        prime_no.append(i)
        print(i,"it is prime number")
print("prime number is :-")       
print(prime_no)



fact=1

n=5

for i in range(1,6):
    fact=fact*i
print(fact)
