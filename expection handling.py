#exception handling

#exception ------> error we use this to slove the error and run the program and continue
# Two tympe :- 1.complie time error,#
               #2.runtime error

#print(10/2) ---> not got any error this program is runing so no error

# run time e.g
#print(a)-->NameError: name 'a' is not defined

#complie time error
#print(a     ---> )was not closed


#try -except this to block
'''
#1. if got any error than print below except statment

try:
    print(a) #critical code
except:
    print("exception handeled")


#2. print exception in one variable

print("code before execution")
try:
    print(a)
except Exception as e:  #catching out error in output formate
    print(e)

#3. write somthing in except below if not given that will gives error

try:
    print(a)#critical code

except:
    #pass

    print("exception handeled")

print("code after excution")

#4.

try:
    print(a)
except:
    pass
finally:
    print("always getting excuted")
print("code after excution")


try:
    print(x)
    
except NameError:

     print("variable is not defined")
except:
    
    print("something else want wrong")
'''
'''(

#finally e.g


try:
    print(x)
    1/0
    
except:
    print("something went wrong")
    1/0
    '''
'''finally:
    print("the 'try except' is finishing")
    1/00'''
'''
try:
    f=open("demofile.txt")
    f.write("world")
except:
    print("somthing went wrong when writting to the file")
finally:
    f.close()

    #thenprogram can continue. without leavimg the file object open



try:
    a=int(input("enter your table number"))
    print("table ")
    for i in range(1,11):
        print(f"{a}*{i}={a*i}")
except:
    print("incorrect input")
 '''   

class UnderAge(Exception):
    pass
def verify_age(age):
    if int(age)<18:
        raise UnderAge
    else:
        print("age:"+str(age))
verify_age(18)







class Negtivenumber(Exception):
    pass
def number_verify(number):
    if number<=0:
        raise Negtivenumber
    else:
        print("it is positive number")
number_verify(-8)














