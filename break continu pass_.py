#for loop
n=range(1,56)
for n1 in n:
    if n1==40:
        break;
print(n1)




#python continue


numbers=[1,2,3,4,5,6,7,8,9]
pos=0
while pos<len(numbers):
    if numbers[pos]%2==0:
        pos=pos+1
        continue
    print(numbers[pos])

    pos=pos+1
 

#for loop
numbers=range(1,11)
for number in numbers:
    if number==7:
        print("7 is skipped")
        continue
    print("this won't be printed")
    print(number)
    print("is double of")
    print(number*2)

#nasted for loop
words=["apple", "banana", "car", "dolphine"]
for word in words:
    print("the following lines will print each letter of " +word)
    for letter in word:
        print(letter)
        print("")


num=["12","14","156","1456","14789"]
for nums in num:
    print("the following num will print each letter of"+nums)
    for numbs in nums:
        print(numbs)


number=range(1,11)
pos=2
for n in number:
    if pos*num:
        print(pos*num)


for i in range(5):
    if i==2:
        continue
    print(i)


for u in range (20):
    if u==10:
        break
    print(u)


for i in range(5):
    print(i)


for m in range (20):
    if m%2==0:
        continue
    print(m)


for y in range(2*20):
    if y%3==0:
        continue
    print(y)


numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number%2==0:
        continue
    else:
        print(number)
        

n="pooja"
a=n[0:4]
print(a)














