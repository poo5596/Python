#python Sets


myset={"apple","banana","cherry"}
print(myset)

#no duplicate value
b={"apple","apple","apple"}
print(b)


#lenght of set

c=len(myset)
print(c)


#unordered

#unchangeable

#set ieam -data types

a={"apple",2,True}
print(a)

set={True,False,False}
print(set)


set1={"abc",34,True,48,"male"}
print(set1)


ser={True}
print(ser)


s={"apple",False,0}
print(s)


#type

#set
myset={"apple","banana","cherry"}
print(type(myset))

'''
#dic
m={"a":"b","a":"c","a":"c"}
print(type(m))

#tuple
r=("a","b","c")
print(type(r))

#list
u=[1,"apple","w"]
print(type(u))

#string
ur="apple"
print(type(ur))


#set()constructor


#tuple/set
bb=set(("apple","banana","cherry"))
print(bb)

#set/tuple
ll=tuple({"apple","banana"})
print(ll)


#set/Dictionary

oo=dict({"apple","banana","oo","urr"})
print(oo)

rr=set({"apple":"bananna","mango":"rr"})
print(rr)


#set\list

yy=list({1,2,3,4,5,})
print(yy)

tt=set([1,2,3,4,5])
print(tt)


#list\tuple

ii=list(("a","c","n"))
print(ii)

kk=tuple(["aa","nn"])
print(kk)
'''

#access set items

pp={"apple","banana",1,}
for y in pp:
    print(y)



#add new items

pp.add("orange")
print(pp)


#update

p={1,2,3}
pp.update(p)
print(pp)

#iterable
r=["apple","banana"]
p.update(r)
print(p)

#remove set

w={"pp",3,True,"apple","banana"}
w.remove(True)
print(w)


#discard
w.discard("apple")
print(w)

#pop
w.pop()
print(w)



#delet
del w
print(w)



#clear
we={"ap" "ab","ac"}
we.clear()
print("its clear")


#join 2 sets
set1={"a","s","x",5}
set2=(1,2,3,4,5,6,"a")
set3=set1.union(set2)
print("set3 is",set3)



set1.update(set2)
print(set1)


#duplicate value

x={"apple","banana","cherry"}
y={"gogle","microsoft","apple"}
x.intersection_update(y)
print(x)

e=x.intersection(y)
print(e)


#keep all, but not the duplicates

x={"apple","banana","cherry"}
y={"google","mirosoft","apple"}
x.symmetric_difference_update(y)
print(x)

#new set in symmetric difference()

x={"apple","banana","cherry"}
y={"gogle","microsoft","apple"}
z=x.symmetric_difference(y)
print("z:-",z)











