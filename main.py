import random

# print(random.choice(['apple', 'banana', 'cherry']))

# This is a sample Python script that prints a random fruit from a list.
type = type(random.choice(['apple', 'banana', 'cherry']))
# print(type)  # This will print: <class 'str'>


def is_adult2(age): #ternary operator
  return True if age > 18 else False

# print(is_adult2(20))  # This will print: True

# print("****************************")

name = "John \" doe"
# print(name.lower())  # This will print: john doe
# print(name.upper())  # This will print: JOHN DOE
# print(name.title())  # This will print: John Doe
# print(len(name))    # This will print: 8
# print("n" in name)  # This will print: False
# print(name[-1].upper())  # This will print: E
# print(name[1:2])  # This will print: o

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
# print(read_any_book)  # This will print: True

# print("**************Math**************")

# print(abs(-7.25))  # This will print: 7.25
# print(pow(3, 2))   # This will print: 9
# print(max(4, 6))   # This will print: 6
# print(min(4, 6))   # This will print: 4
# print(round(3.7))  # This will print: 4
# print(round(3.445,2))  # This will print: 3

# print("**************Enum**************")   
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class State(Enum):
    START = 1
    RUNNING = 2
    PAUSED = 3
    STOPPED = 4

# print(State.START.value)  # This will print: State.START
# print(State.START.name)   # This will print: 1
# print(State(1))          # This will print: State.START
# print(State['START'])    # This will print: State.START

# print(len(State))  # This will print: 4  


# print("**************List Operations**************")
dogs = ['Buddy', 'Max', 'Bella', 'Charlie']
dogs.append('Lucy')
dogs.append('Daisy')
# print(dogs) 
dogs.extend(['Molly', 'Bailey'])
#dogs += ['Molly', 'Bailey']
dogs.index('Bella')  # This will return the index of 'Bella' in the list.
dogs.insert(2, 'Rocky')  # This will insert 'Rocky' at index 2.
dogs.sort(key=str.lower)  # This will sort the list of dogs in alphabetical order, ignoring case.
# print(dogs)  # This will print the list of dogs with 'Lucy' and 'Daisy' added.
itemsCopy = dogs[:5]
# print(itemsCopy)  # This will print a copy of the list of dogs.
# print(sorted(itemsCopy, key=str.lower, reverse=True))

# print("**************tuple Operations**************")
names = ("Alice", "Bob", "Charlie")


dog = {"name": "Buddy", "age": 3, "breed": "Golden Retriever"}
# print(dog["name"])  # This will print: Buddy

# print(dog.items())  # This will print all key-value pairs in the dictionary.
# print(dog.keys())   # This will print all keys in the dictionary.
# print(dog.values()) # This will print all values in the dictionary.


del dog['age']
# print(dog)  # This will print the dictionary without the 'age' key.

# print("**************Sets**************")
set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "banana"}

# print(set1)  # This will print the elements of set1 as a list.

# print("**************Functions Inner/outer**************")

phrases = ["Hello, world!", "Python is great.", "I love programming.", "Have a nice day!"]

# for phrase in phrases:
#     print(phrase)

def count():
    count = 0

    def inner_increment():
        nonlocal count
        count += 1
        print(count)
    inner_increment()


# print(count())  # This will print: None


# print("************** Closuers **************")
def outer_function():
    count = 0
    def inner_function():
        nonlocal count
        count += 1
        return count
    return inner_function

closure = outer_function()
# print(closure())  # This will print: 1
# print(closure())  # This will print: 2
# print(closure())  # This will print: 3



# print("************** Loops **************")
# for i in range(10):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# isOnline = True
# while isOnline:
#     print("User is online")
#     isOnline = False

# items = ['apple', 'banana', 'cherry']
# for index, item in enumerate(items):
#     print(f"Index: {index}, Item: {item}")



# print("************** Classes **************")

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self,tag="None"):
        return f"{self.name}" + " Woof!" + f" Tag: {tag}"
# animal = Animal("Generic Animal")


# print(animal.speak()) 

# print("************** Modules **************")

import dog
from dog import dok_speek
dog_sound = dok_speek()
# print(dog_sound)  # This will print: Woof! Woof!

import sys

x = [3, 6, 9, 12, 15]
# print(sys.getsizeof(x))  # This will print the size of the list x in bytes.


# import argparse

# parser = argparse.ArgumentParser(
#     description="A simple example of argparse usage."
# )

# parser.add_argument(
#     '-n',
#     '--name',
#     metavar='name',
#     required=True,
#     choices=['Alice', 'Bob', 'Charlie'],
#     help='this is the name argument'
# )

# args = parser.parse_args()

# print(f"Hello, {args.name}!")

# print("************** Lamdba Function **************")
square = lambda num : num * num
malti = lambda a , b : a * b
add = lambda a, b , c : a + b + c

# print(square(34))
# print(malti(4,5))
# print(add(2,3,4))

# print("************** Map, Filterm Reduce Functions **************")

numbers = [1,2,3,4,5,6,7,8,9,10]
# def double(num):
#     return num * 2

double = lambda num: num * 2

result = list(map(double, numbers))
# print(result)  # This will print: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

isEven = lambda num: num % 2 == 0

filteredResult = list(filter(isEven, numbers))
# print(filteredResult)  # This will print: [2, 4, 6, 8, 10]


expenses = [
    ('January', 2200),
    ('February', 2350),
    ('March', 2600),
    ('April', 2130),
    ('May', 2190)
]

sum = 0
for month, expenses in enumerate(expenses):
    sum += expenses[1]

# print(f"Total expenses: {sum}")  # This will print: Total expenses: 11470


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 1 or n == 0 :
        return 1
    else:
        return n * factorial(n - 1)
# print(factorial(4))

# print("************** Decorators **************")

def log(fun):
    def wrapper(*args, **kwargs):
        print(f"Function '{fun.__name__}' is called with arguments: {args} {kwargs}")
        result = fun(*args, **kwargs)
        print(f"Function '{fun.__name__}' returned: {result}")
        return result
    return wrapper
@log
def add(a, b):
    return a + b

# print(add(3, 5))  # This will print the log messages along with the result 8

# print("************** Docstrings **************")
# print("************** Annotations **************")

def increment(n:int) -> int:
    return n + 1

count: int = 0

def greet(nam: str) -> str:
    return f"Hello, {name}!"

name: str = "Alice"
greeting: str = greet(name)


# print("************** Exceptions **************")

try: 
    result = 2 / 1
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else: 
    print(f"Result: {result}")
finally:
    print("Execution completed.")

class CustomError(Exception):
    print("This is a custom error message.") 
    pass

class DogNotFoundError(Exception):
    print("Dog not found in the database.")
    pass


try:
    raise DogNotFoundError()
except DogNotFoundError as e:
    print("Caught a DogNotFoundError:", e)

filename = 'non_existent_file.txt'

try: 
    file = open(filename, 'r')
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"Error: The file '{filename}' was not found.")
else :
    file.close()
finally:
    print("Finished attempting to read the file.")

# print("************** List Comprestions **************")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_power_2 = [n**2 for n in numbers]
# print(numbers_power_2)  # This will print: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


class Dog:
    def eat(self):
        return "The dog is eating."
    
class Cat:
    def eat(self):
        return "The cat is eating."
    
