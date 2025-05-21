#list comprehensions in python are a concise way to create a lists.
#they allow you to generate a new lisy by applying an expression to each item in an
#existing iterable (e.g, a list, tuple, or range) and optionally filter the terms

#based on a condition.
#iterable and iterator


#1.creating a list of squares

#using for loop
squares=[]
for i in range(1,6):
    squares.append(i**2)
print(squares)

#using list comprehension
squares=[i**2 for i in range(1,6)]
print(squares)


#2. filtering even numbers


even_numbers=[]
for num in range(1,20):
    if num%2==0:
        even_numbers.append(num)
print(even_numbers)

#using list comprehension with a  condition
even_numbers=[num for num in range(1,40)if num%2==0]
print(even_numbers)


#3.creating a list of uppercase words
upper_words=[]
words=["apple","banana","mango","oragne"]
for word in words:
    upper_words.append(word.upper())
print(upper_words)

#using comprehension
word=["Apple","Bnnana","Mango","Oragne"]
lower_word=[words.lower() for words in word]
print(lower_word)

#4. using a function a list comprehension


def double(num):
    return num*2

numbers=[1,2,3,4,5,6]
doubled_numbers=[double(num) for num in numbers]
print(doubled_numbers)

now=[]
numbers=[1,2,3,4]
for num in numbers:
    now.append(double(num))
print(now)
    
       
