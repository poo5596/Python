
#list(data structure)

thislist=["apple", "banana", "cherry"]
print(thislist)

#print 2nd item

print(thislist[1])

#change 2nd item
thislist[1]="mango"
print(thislist)


#loop through list item in one by one

for x in thislist:
    print(x)


#check if item is exit or not

if"mango" in thislist:
    print("yes, 'mango' is in the fruits list")

else:
    print("no, 'mango' is not in the fruits list")



#list length

print(len(thislist))

#add item using append method

thislist.append("orange")
print(thislist)


#insert item using insert menthod

thislist.insert(2,"bluebarry")
print(thislist)


#remove item

thislist.remove("bluebarry")
print(thislist)


#pop() method delete

thislist.pop()
print(thislist)


#del keyword removes / delete

del thislist[2]
print(thislist)


#del keyword delete all list
b=["apple", "banana", "cherry"]


del b
#print(b)

#clear() method empties

a=["apple", "banana","cherry"]
a.clear()
print(a)


#extend 

fruits=["apple", "banana", "cherry"]
points=(1,4,5,9)
fruits.extend(points)
print(fruits)




#append

number=[1,2,3,4,5,]
number.append(45)
print(number)


a=['a','b','c',]
a.append('p')
print(a)


x=[1,2,3,4,5]
y=[6,7,8,9,10]
x.append(y)
print(x)


a=["apple","banana","cherry"]
b=("Ford","BMW","Volvo")
a.append(b)
print(a)


#clear

fruits=["apple","banana","cherry"]
fruits.clear()
print(fruits)

#copy
fruits=["apple","banana","cherry"]
x=fruits.copy()
print(x)

#count#

num=[1,2,2,4,5,7,8,9,9,9,4,5,6,]
y=num.count(5)
print(y)

#extend #

fruits=["apple","banana","cherry"]
points=["1","4","5","9"]
fruits.extend(points)
print(fruits)

#index #

num=[4,55,64,32,16,32]
x=num.index(32)
print(x)


#insert ###
fru=["apple","banana","cherry"]
fru.insert(2,"oragane")
print(fru)


#reverse #

fruits=["apple","banana","cherry"]
fruits.reverse()
print(fruits)



#sort#
cars=[1,4,5,7,9]
cars.sort()
print(cars)


# pop if print any variable so print give thst pop only
fruits=["apple","banana","cherry"]
fruits.pop(1)
print(fruits)


# remove#
fruits=["apple","banana","cherry"]
fruits.remove("banana")
print(fruits)



    
                                                                                                                                                                                                                                                                                                                                                                                                                        


