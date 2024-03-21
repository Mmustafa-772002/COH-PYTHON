# function and recursion -a function is used to perform a specific task.
# such as a function to add two numbers, a function to print the name, etc.

# def my_function():
#     print("hello")
#
# my_function()

# def my_function(name):
#     print("hello " + name)
#
# my_function("harry")

marks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentage = (sum(marks) / 10) * 100

marks1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentage1 = (sum(marks) / 10) * 100
print(percentage, percentage1)


# q - write a function to add two numbers
def add(a, b):
    return a + b


def percentage(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4]) / 500) * 100
    return p


marks1 = [45, 75, 99, 62, 66]
percentage1 = percentage(marks1)

marks2 = [75, 99, 62, 66, 45]
percentage2 = percentage(marks2)

print(percentage1, percentage2)


#  q- input name in the function and print the name in the function
# def my_function(name):
#     print("hello " + name)


# my_function(name=input("enter the name: "))

# to print the name in the function
# def hello(name ):
#     print("hello "+name )

# hello("harry")

# def hii(name):
#     print("hii "+name)
#     print("welcome to the function, "+name)
#     return name

# hii(name=input("enter the name:"))

# types of the function in the python
# 1. built in function
# 2. user defined function

# built in function - the function which are already defined in the python are called built in function
# for example - print(), input(), sum(), max(), min(), len(), etc.
# list of the built in function in the python
# abs() , all(), any(), ascii(), bin(), bool(), bytearray(), bytes(), callable(), chr(), classmethod(), compile(), complex(), delattr(), dict(), dir(), divmod(), enumerate(), eval(), exec(), filter(), float(), format(), frozenset(), getattr(), globals(), hasattr(), hash(), help(), hex(), id(), input(), int(), isinstance(), issubclass(), iter(), len(), list(), locals(), map(), max(), memoryview(), min(), next(), object(), oct(), open(), ord(), pow(), print(), property(), range(), repr(), reversed(), round(), set(), setattr(), slice(), sorted(), staticmethod(), str(), sum(), super(), tuple(), type(), vars(), zip(), __import__()
# abs() - returns the absolute value of the number
# example :
print(abs(-7.25))
# all() - returns true if all items in an iterable are true
# itrable means - list, tuple, set, dictionary, etc.
# example :
x = [1, 2, 3, 4]
print(all(x))

x = [0, 1, 2, 3]
print(all(x))

x = (1, 2, 3)
print(all(x))


# any() - returns true if any item in an iterable is true
# example :
x = [0, 1, 2, 3]
print(any(x))

# ascii() - returns a readable version of an object. replace non-ascii characters with escape character
# example
x = ascii("My name is Ståle")
print(x)

# bin() - returns the binary version of the number
# example =
bin(36)
# bool() - returns the boolean value of the object
# example
example = bool(0)
print(example)

# bytearray() - returns an array of bytes
# example :
a = bytearray(5)
print(a)

# bytes() - returns a bytes object
# example :
a = bytes(5)
print(a)
# callable() - returns true if the object is callable, otherwise false
a = 5
print(callable(a))

# chr() - returns a character from the specified unicode
a = chr(97)
print(a)


# classmethod() - converts a method into a class method
class MyClass:
    @classmethod
    def my_method(cls):
        pass


a = MyClass.my_method()

# compile() - returns the specified source as an object, ready to be executed
a = compile("print(55)", "test", "eval")
exec(a)

# complex() - returns a complex number
a = complex(3, 5)
print(a)


# delattr() - deletes the specified attribute from an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


harry = Person("Harry", 25)
delattr(harry, "age")

# dict() - returns a dictionary
a = dict(name="harry", age=25)
print(a)

# dir() - returns a list of the specified object's properties and methods
a = dir("harry")
print(a)

# divmod() - returns the quotient and the remainder when argument1 is divided by argument2
a = divmod(5, 2)
print(a)

# enumerate() - takes a collection (e.g. a tuple) and returns it as an enumerate object
x = ("apple", "banana", "cherry")
y = enumerate(x)
print(list(y))

# eval() - evaluates and executes an expression
x = 1
print(eval("x + 1"))

# exec() - executes the specified code (or object)
# example :
x = 'name = "John"\nprint(name)'
exec(x)

# filter() - use a filter function to exclude items in an iterable
# example :
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)
for x in adults:
    print(x)

# float() - returns a floating point number
# example :
a = float(3)
print(a)

# format() - formats a specified value
# example :
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# frozenset() - returns a frozenset object
# example :
a = frozenset({"apple", "banana", "cherry"})
print(a)


# getattr() - returns the value of the specified attribute
# example :
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = getattr(Person, "age")
print(x)

# globals() - returns the current global symbol table as a dictionary
# example :
x = globals()
print(x)


# hasattr() - returns true if the specified object has the specified attribute
# example :
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = hasattr(Person, "age")
print(x)

# hash() - returns the hash value of a specified object
# example :
x = hash("hello")
print(x)

# help() - executes the built-in help system
# example :
x = help(print)

# hex() - converts a number into a hexadecimal value
# example :
a = hex(255)
print(a)

# id() - returns the id of an object
# example :
a = 5
print(id(a))

# input() - allows user input
# example :
print("Enter your name:")
x = input()
print("Hello, " + x)

# int() - returns an integer number
# example :
a = int(3.5)
print(a)

# isinstance() - returns true if the specified object is an instance of the specified object
# example :
x = isinstance(5, int)
print(x)


# issubclass() - returns true if the specified object is a subclass of the specified object
# example :
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = issubclass(Person, object)
print(x)

# iter() - returns an iterator object
# example :
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# len() - returns the length of an object
# example :
a = len("hello")
print(a)

# list() - returns a list
# example :
a = list(("apple", "banana", "cherry"))
print(a)

# locals() - returns an updated dictionary of the current local symbol table
# example :
x = locals()
print(x)


# map() - returns the specified iterator with the specified function applied to each item
# example :
def myfunc(n):
    return len(n)


x = map(myfunc, ("apple", "banana", "cherry"))
print(list(x))

# max() - returns the largest item in an iterable
# example :
a = max(5, 10, 25)
print(a)

# memoryview() - returns a memory view object
# example :
x = memoryview(b"Hello")
print(x)

# min() - returns the smallest item in an iterable
# example :
a = min(5, 10, 25)
print(a)

# next() - returns the next item in an iterator
# example :
mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))
print(next(mylist))
print(next(mylist))

# object() - returns a new object
# example :
x = object()
print(x)

# oct() - converts a number into an octal
# example :
a = oct(8)
print(a)

# open() - opens a file and returns a file object
# example :
f = open("demofile.txt", "r")
print(f.read())

# ord() - converts a character into the unicode
# example :
a = ord("h")
print(a)

# pow() - returns the value of x to the power of y
# example :
a = pow(4, 3)
print(a)

# print() - prints the specified message to the screen
# example :
print("Hello, World!")


# property() - gets, sets, deletes a property
# example :
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)


p = Person("Adam")
print(p.name)
p.name = "John"
print(p.name)
del p.name

# range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# example :
a = range(6)
print(a)

# repr() - returns a readable version of an object
# example :
a = repr("Hello")
print(a)

# reversed() - returns a reversed iterator
# example :
a = reversed("hello")
print(list(a))

# round() - rounds a number
# example :
a = round(5.76543, 2)
print(a)

# set() - returns a new set object
# example :
a = set(("apple", "banana", "cherry"))
print(a)


# setattr() - sets the value of the specified attribute of the specified object
# example :
class Person:
    name = "John"
    age = 36
    country = "Norway"


setattr(Person, "age", 40)
print(Person.age)

# slice() - returns a slice object
# example :
a = slice(3)
print(a)

# sorted() - returns a sorted list
# example :
a = sorted([36, 5, -12, 9, -21])
print(a)


# staticmethod() - converts a method into a static method
# example :
class Person:
    age = 25

    @staticmethod
    def hello():
        print("Hello, I am 25 years old")


Person.hello()

# str() - returns a string object
# example :
a = str(3)
print(a)

# sum() - returns the sum of all items in an iterable
# example :
a = sum([1, 2, 3])
print(a)


# super() - returns an object that represents the parent class
# example :
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

# tuple() - returns a tuple
# example :
a = tuple(("apple", "banana", "cherry"))
print(a)

# type() - returns the type of an object
# example :
a = type(3)
print(a)


# vars() - returns the __dict__ property of an object
# example :
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = vars(Person)
print(x)

# zip() - returns an iterator, from two or more iterators
# example :
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(tuple(x))

# __import__() - imports the specified module
# example :
import math

x = __import__("math", globals(), locals(), [], 0)
print(x)


# user defined function - the function which are defined by the user are called user defined function
# example :
def my_function():
    print("hello")


my_function()


def my_function(name):
    print("hello " + name)


my_function("harry")


def my_function(name):
    print("hello " + name)


my_function(name="h arry")


def my_function(name):
    print("hello " + name)


my_function(input("enter the name: "))

# recursion - a function calling itself is called recursion. it is used to solve the complex problem by dividing it into smaller problems.

# example :

n = 5
product = 1
for i in range(n):
    product = product * (i + 1)
print(product)
