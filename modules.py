#modules

#modules is a container with have many function in bulid if we have to use that then import moudles


#1.create----> user defined modules

#file Name---> modules.py
'''

def greeting(name):
    print("hello"+name)

import modules
modules.greeting("pooja")'''



#2. use modules

'''import modules
modules.greeting("pooja")

import math
q=math.log(67)
print(q)'''

#3.  Variables in module


person1={
    "name":"pooja",
    "age":25,
    "country":"India"
    }

import modules
a=modules.person1["age"]
print(a)


name=("apple","banana","mango")
import modules
b=modules.name[0]
print(b)

name=("apple","banan","mango")
b=name[0]
print(b)


#4 name change in modules

person1={
    "name":"pooja",
    "age":25,
    "country":"India"
    }

import modules as i
a=i.person1["age"]
print(a)


'''#5. built -in modules

import platform
x=platform.system()
print(x)

import platform
x=dir(platform)
print(x)'''


#6. import from modules  # if we have to fine any one modules


def greeting(name):
    print("hello,"+name)

person1={
    "name":"jonh",
    "age":"36",
    "country":"norway"
    }

from modules import person1
print(person1["age"])


from modules import greeting
greeting("pooja")











