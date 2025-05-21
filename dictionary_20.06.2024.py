thisdict={
    "brand": "ford",
    "model": "mustang",
    "year" : 1964
    }

print(thisdict)

#accessing items 1st method
x=thisdict["model"]
print(x)

x=thisdict["year"]
print(x)

#2nd method

b=thisdict.get("year")
print(b)


#change value
thisdict["year"]=1982
print(thisdict)


thisdict["brand"]="pooma"
print(thisdict)


#loop in dictionary

for r in thisdict:
    print(r)


#check if key exists

if "year" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict dictionary")


#len of dictionary

    print(len(thisdict))

#additing item

thisdict["colour"]="red"
print(thisdict)


#removing items

thisdict.pop("model")
print(thisdict)


thisdict.popitem()
print(thisdict)


del thisdict["year"]
print(thisdict)


#clear

company={
    "a":"apple",
    "b":"banana",
    "c":"cherry"
    }

#company.clear()
#print(company)

#copy

r=company.copy()
print(r)


#fromkey note: this funcation conved variable into us dictionary 

m=('key1',"key2","key3")
n=1
comp=dict.fromkeys(m,n)
print(comp)


#get

w=company.get("a")
print(w)


#items


q=company.items()
print(q)


w=company.items()
company["b"]=1980
print(w)

#keys
r=company.keys()
print(r)


#pop

company.pop("a")
print(company)


#popitem

company.popitem()
print(company)

#setdefault######
company={
    "a":"apple",
    "b":"banana",
    "c":"cherry"
    }
t=company.setdefault("b","white")
print(t)



#update

company.update({"colour":"red"})
print(company)


company.update({"colour" : "pink"})
print(company)

#values

u={
    "y":"pooja",
    "o":"kajal",
    "l":"yogesh"
    }


x=u.values()
u["o"]=1985
print(x)






    

    
