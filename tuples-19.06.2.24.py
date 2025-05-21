thistuple=("banana","apple","cherry")
print(thistuple)

#count

r=(1,2,3,4,5,6,2,2,2)
y=r.count(2)
print(y)

y=("apple","banana","apple","apple")
o=y.count("apple")
print(o)


o=(1,3,7,8,7,5,4,6,8,5)
t=o.count(5)
print(t)

#index

w=("apple","banana","oragne")
x=w.index("banana")
print(x)

r=(1,2,3,4,5,6,7,8)
q=r.index(4)
print(q)


ytuple=(1,3,7,8,7,5,4,6,8,5)
w=ytuple.index(8)
print(w)

#for loop

for n in r:
    print(n)

for u in ytuple:
    print(u)

#you can access tuple item by using index no.
    
print(thistuple[1])

#item exists
y=("apple", "banana","mango")
if"apple" in y:
    print("yes, 'apple',is in the y tuple")

#len in tuple
q=(1,2,3,4,5,6)
print(len(q))

#del tuple
p=(1,2,3,4,5,6)
del p
print(p)

#below funcation are not working in tuple

point=(1,2,3,4,5)
thistuple.extend(point)
print(thistuple)


thistuple.append("oragane")
print(thistuple)

thistuple.clear()
print(thistuple)


thistuple.sort()
print(thistuple)

y=thistuple.copy()
print(y)

thistuple[1]="blackcurrant"
print(thistuple)




