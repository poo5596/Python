
#FUNCTIONS: set of instructions to perform a particular task its  run only after call 
#two types : 1. built in
          #  2. user defined

#def: ek keyword, fn create karte hai

#paranthesis()......display......> name of your fn, def


#fn creation

#non-parameterize fn

'''def display():

    print("hello world")  #to print hello world
#fn call
display()
display()
display()


#parameterize fn
def add(n1,n2):
    print(n1+n2)

add(2,3)
add(5,6)

#user define

n1=int(input("enter value of n1"))
n2=int(input("enter value of n2"))


def addi(a,b):
    print(a+b)
addi(n1,n2)


m1=int(input("enter value of m1"))
m2=int(input("enter value of m2"))
def multiple(q,r):
    print(q*r)
multiple(q,r)



def play(a,b):
    print(a+b)
play(1,3)


m1=int(input("enter value of m1"))
m2=int(input("enter value of m2"))
def multiple(m1,m2):
    print(m1*m2)
multiple(m1,m2)




para : m1,m2
arg : m1,m2

multiple(m1,m2) # local var, #parameters
fn: parameterised fn, fruitful fn

add() # non para ,void fn'''

'''
# return

def add(a,b):
    return a+b
    #print(a+b)
    
result=add(2,3)#call
print(result)

print(add(2,3))

#return ----> fn call usko print karna padega




def subtration(w,t):
    return w-t

print(subtration(8,15))




def multipication(d,e):
    return d*e
print(multipication(2,9))




def division (t,y):
    return t*y
print(division(14,2))


def floor_division (p,o):
    return p//o
print(floor_division(12,3))

'''

'''

def add():
    a=10
    b=50
    print(a+b)


def multi():
    i=20
    j=30
    print(i*j)

add()
multi()


'''

'''
a=int(input("enter value m"))
b=int(input("enter value n"))

def add(m,n):
    return(m+n)

print(add(a,b))
'''

'''
a=20
b=30
def multi(m,n):
    return(m+n)

print(multi(a,b))
    


def add():
    w=20
    e=56
    print(w+e)
    return(w+e)
print(add())
'''

'''
a=1
b=35
c=50
def gradtest(a,b,c):
    
    if(a>b and a>c):
        print("a is gradtest number",a)
    elif (b>c and b>c):
        print("b is gradtest number",b)
    else:
        print("c is gradtest number",c)


gradtest(a,b,c)




'''

'''
def displayValue1():
    global a
    a=100
    print("inside first fn:",a)
    return a
displayValue1()
print(a)


def add():
    global a
    a=100
    print("value inside fn",a)
add()
print("outside fn",a)
'''

'''
def local():
    x=10
    print(x)
local()

#return with no parameter
def local():
    x=20
    return x
print(local())


bb=55
def gh():
    print(bb)
gh()


e=10005
def hello():
    global w
    w=56
    print("local variable", w)
    print("global value",e)
hello()
print(e)
print(w)

'''

    
'''

#local & global var
x=10

def f1():
    global x
    print("local var is : ",x)
    print("global var inside fn : ",x)
f1()
print("global VAR outside fn ",x)






#default parameter value

def my_function(country="norway"):
    print("I am from "+ country)
my_function("sweden")
my_function("India")
my_function()
my_function("Brazil")




#nasted fn without parameter

#without run outerfn innerfn will not run

def outerfn():
    print("outer fn")

    def innerfn():  #we call inner fn inside the fn becoz we call fn in above def 
        print("inner fn") #inner fn call only inside 
    innerfn() #if we dont wont to print inner fn you can comment out or you not print ok
outerfn()


    

def outerfn(s,w):
    print(s+w)

    def innerfn(a):
        print(a)
    innerfn(7)

outerfn(8,9)
'''



#types of arguments- 1.default argu 2.arbitary arug, 3.keyword arug

#defult arugments

def defult(country="India"):
    print(country)

defult() #e.g of defuly arguments
defult("Island")
defult("Dubai")
defult("USA")



#arbitray arguments (it is veriable lenght arugument)


'''
#e.g paremeter overloading that why we will use arbitray arug to store multiple arug

def displayNaturalNoSeries(a,b,c,d,e,f):#e.g paremeter overloading
    print(a,b,c,d,e,f)
displayNaturalNoSeries(1,2,3,4,5,6)'''


def displayNaturalNoSeries(*num): #(* i can store all arugment in one parement)
    print(num)
    #print(type(num))
    #for i in num:
       #print(i, end=" ")
displayNaturalNoSeries(1,2,3,4,5,6,7,8)

#if i want to store muliple arugement is single parameter
#for that i need to make my para arbitary





#keyword argument

#when calling a function, you can specify the value of an argument by its parameter name.
#that is know as a keyword arugment.


def series(a,b,c):
    print(a,b,c)
series(a=1, c=3, b=45)
series(1,3,45)























    

    
























