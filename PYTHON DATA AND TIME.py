lip#python data and time


import datetime
x=datetime.datetime.now()
print(x)  #date day year and time


import datetime
x=datetime.datetime.now()
print(x.year)   #print current year
print(x.strftime("%A"))  #print today day


#creating date object

import datetime
x=datetime.datetime(2024,7,25) #print in year formate
print(x)


#strftime ()method

import datetime
x=datetime.datetime(2024,7,25)
print(x.strftime("%B"))  #prin month


x=datetime.datetime.now()
print(x.strftime("%a")) #print(day in short formate)

x=datetime.datetime.now()
print(x.strftime("%A"))#print(day )

x=datetime.datetime.now()
print(x.strftime("%w")) #day in o-6 print

x=datetime.datetime.now()
print(x.strftime("%d")) #date


x=datetime.datetime.now()
print(x.strftime("%b")) #month short version

x=datetime.datetime.now()
print(x.strftime("%B")) #month full varison


x=datetime.datetime.now()
print(x.strftime("%m")) #date






