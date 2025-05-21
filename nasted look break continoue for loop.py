#while loop statement e.g
#ok
'''
cnt=1
while cnt<5:
    print(cnt)
    print("This is inside of while loop")
    cnt+=1
else:
    print(cnt)
    print("this is outside of while loop")


#ok

word="anaconda"
pos=0#initial position is zero
while pos<len(word):
    print(word[pos])
    #increment the position after printing the letter of that position
    pos+=1


'''
#nasted while loop

line=1
while line<=5:
    pos=1
    while pos<line:
        print(pos)
        pos+=1
    else:
        print(pos)
        line+=1



#python break

number=1
while True:
    print(number)
    number+=2
    if number>10:
        break;  
print(number)

'''
'''
#ok

words=["ran", "sun", "moon", "exit", "weather"]
for word in words:
    if word=="exit":
        break;
    print(word)


#ok
number=[1","2","3","4","5","6","7","8","9","12"]
for num in number:
    if num=="9":
        break;
    print(num)
'''

'''
###error
n=range(1,56)
print(n)
for n1 in n:
    if n1==40:
        break;
    print(n1)




#python continue

########erro
numbers=[1,2,4,3,6,5,7,10,9]
pos=0
while pos<len(numbers):
    if numbers[pos]%2==0:
        pos=pos+1
        continue
    print(numbers[pos])

    pos=pos+1
    


numbers=range(1,11)
for number in numbers:
    if number==7:
        print("7 is skipped")
        continue
    print("this won't be printed")
    print(number*2)
    print("is double of")
    print(number)

