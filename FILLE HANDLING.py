'''#read mode 
f=open("demofile.txt","r")
print(f.read())

#write mode
f=open("demofile.txt","w")
f.write("pooja gupta")


#read mode 
f=open("demofile.txt","r")
print(f.read())

#append

f=open("demofile.txt","a")
f.write("data analytics")

#read mode 
f=open("demofile.txt","r")
print(f.read())


#create a file

f=open("pooja1.txt","x")

# write a file
f=open("pooja1.txt","w")
f.write("pooja gupta")

#read a file 
f=open("pooja1.txt","r")
print(f.read())

#create
q=open("work.txt","x")

#write
q=open("work.txt","w")
q.write("i am good")
q=open("work.txt","r")
print(q.read())

q=open("work.txt","a")
q.write("very good")

q=open("work.txt","r")
print(q.read())

q=open("work.txt","w")
q.write("delet and replace")

q=open("work.txt","r")
print(q.read())

q=open("work.txt","a")
q.write("{a}+{b} value of a=10 and b=20")

q=open("work.txt","r")
print(q.read())


#delete folder


import os
os.remove("demofile.txt")


import os
os.remove("pooja1.txt")

'''





