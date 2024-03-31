# oops  - solving a problem byy creating object is one of the most common way to solve the problems in python.
class number:
    def sum(self):
        return self.a + self.b


num = number()
num.a = 1
num.b = 24
s = num.sum()
print(s)


# class is a blueprint for the object and object is an instance of the class.

# class syntax:
# pascal case - class name should start with the capital letter.
# class name should start with the capital letter.
# class should have a method with a self parameter.
# EmployeeName --> PascalCase

# camelClass : the first letter of the word should be small and the first letter of the second word should be capital.

# camelCase --> employeeName
# snake_case : the first letter of the word should be small and the first letter of the second word should be small.
# snake_case --> employee_name


# method and variables are called attributes of the class.

# object : a object is an instance of the class. object is a real world entity. object is a physical entity. object is a runtime entity. object is a memory entity.   when the class is define the memory is allocated to the object

# object of an class is created by the class name followed by the parenthesis.

# from git import Remote
# import pandas as pd

# pd.DataFrame()

# class RailwayForm:
#     formType = "RailwayForm"

#     def printData(self):
#         print(f"name is {self.name}")
#         print(f"train is {self.train}")


# harryapplication = RailwayForm()
# harryapplication.name = "Harry"
# harryapplication.train = "Rajdhani Express"
# harryapplication.printData()


# class player:
#     def moveRight(self):
#         pass

#     def moveLeft(self):
#         pass

#     def moveUp(self):
#         pass


# remote1 = Remote()
# player1 = player()

# if remote1.isLeftPassed():
#     player1.moveLeft()

# if remote1.isRightPassed():
#     player1.moveRight()

# if remote1.isUpPassed():
#     player1.moveUp()

# oops is used for the to create the real world entity.

# abstraction: hiding the complexity of the code and showing the only the necessary things to the user is called abstraction. the abstraction is used in the oops to hide the complexity of the code.

# encapsulation: binding the data and the function together is called encapsulation.

# inheritance: the property of the parent class is inherited by the child class is called inheritance.

# polymorphism: the same function name is used for the different purpose is called polymorphism.

# modeling a problem in oops :

# Step 1: Identify the objects: These are usually the nouns in the problem description.
# Step 2: Identify the attributes: These are the properties or characteristics of the objects.
# Step 3: Identify the behaviors: These are the actions that the objects can perform. They are usually the verbs in the problem description.
# Step 4: Identify the relationships: These are the ways in which the objects interact with each other.

# 1.Objects: Library, Book, Librarian, Member

# 2.Attributes:
#   Library: name, address
#   Book: title, author, ISBN
#   Librarian: name, employeeId
#   Member: name, memberId

# 3.Behaviors:
#   Library: addBook, removeBook
#   Book: borrow, return
#   Librarian: issueBook, receiveBook
#   Member: requestBook, returnBook


# 4.Relationships:
#   A Library has Books
#   A Librarian works at a Library
#   A Member borrows a Book from a Library through a Librarian
class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        self.books.remove(book)


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def borrow(self):
        pass

    def returnBook(self):
        pass


class Librarian:
    def __init__(self, name, employeeId):
        self.name = name
        self.employeeId = employeeId

    def issueBook(self, book):
        pass

    def receiveBook(self, book):
        pass


class Member:
    def __init__(self, name, memberId):
        self.name = name
        self.memberId = memberId

    def requestBook(self, book):
        pass

    def returnBook(self, book):
        pass


# attribute : the property of the object is called attribute. the attribute is the variable of the class.
# example: name, age, address, salary, employeeId, ISBN, title, author

# method : the function of the class is called method. the method is the function of the class.
# example: addBook, removeBook, borrow, returnBook, issueBook, receiveBook, requestBook, returnBook

# self : self is the reference to the object of the class. self is the first parameter of the method of the class. self is the reference to the object of the class.
# example : self.name, self.age, self.address, self.salary, self.employeeId, self.ISBN, self.title, self.author

# __init__ : __init__ is the constructor of the class. __init__ is the special method of the class. __init__ is called when the object of the class is created. __init__ is used to initialize the attribute of the class.
# example: def __init__(self, name, age, address, salary, employeeId, ISBN, title, author):
#     self.name = name
#     self.age = age
#     self.address = address
#     self.salary = salary
#     self.employeeId = employeeId
#     self.ISBN = ISBN
#     self.title = title
#     self.author = author

# class attribute and instance attribute: class attribute is the attribute which is common for all the objects of the class.
# example: formType = "RailwayForm"
# class attribute is the attribute which is common for all the objects of the class.
# example: name, train

# instance attribute is the attribute which is specific to the object of the class.
# example: name = "Harry", train = "Rajdhani Express"


class Employee:
    company = "Google"
    salary = 100


#   class attribute is the attribute which is common for all the objects of the class.
#   example: company = "Google"


harry = Employee()
rajni = Employee()
# harry.salary = 300
# rajni.salary = 400
print(harry.salary)
print(rajni.salary)

# instance attribute is the attribute which is specific to the object of the class.
# example: salary = 300, salary = 400
harry.salary = 300
rajni.salary = 400
print(harry.company)
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)
# print(rajni.address)
# if the address variable is not created then the error is generated.

# if the new instance variable is created then the instance variable is created for the object of the class.

# self : self is the reference to the object of the class. self is the first parameter of the method of the class. self is the reference to the object of the class.
# example: self.name, self.age, self.address, self.salary, self.employeeId, self.ISBN, self.title, self.author


class employee:
    company = "Google"

    def getSalary(self):
        print("the salary is 100k")
        print(f"the salary is {self.salary} in {self.company}")


harry = employee()
harry.salary = 100000
harry.getSalary()
employee.getSalary(harry)

# the use of self is we can use both instance attribute and class attribute in the method of the class.

# the temp code runner file is created to run the code in the visual studio code.

# static method : the method which is not using the self parameter is called static method

# the static method is used to create the utility function. the static method is used to create the utility function.


class employee:
    company = "Google"

    def getSalary(self, signature):
        # the f in the print function is used to format the string.
        print(
            f"the salary for this employee working in {self.company} is {self.salary}\n{signature}"
        )

    @staticmethod
    # the staticmethod is the method which is not using the self parameter. the staticmethod is used to create the utility function.
    def greet():
        print("good morning, sir")


harry = employee()
harry.salary = 100000
harry.getSalary("thanks!")
harry.greet()

# constructor : the constructor is the special method of the class. the constructor is called when the object of the class is created. the constructor is used to initialize the attribute of the class.

# __init__() constructor : __init__() is the constructor of the class. __init__() is the special method of the class. __init__() is called when the object of the class is created. __init__() is used to initialize the attribute of the class.


class employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created !")

    def getDetails(self):
        print(
            f"The name of the employee is {self.name}, salary is {self.salary}, and the subunit is {self.subunit}"
        )


harry = employee("Harry", 100000, "YouTube")
harry.getDetails()


# create a class programmer working at microsoft. the class has the following attributes:
class programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the {self.company} programmer is {self.name} and the product is {self.product}"
        )


harry = programmer("harry", "skype")
alka = programmer("alka", "github")
harry.getInfo()
alka.getInfo()

# write a class calculator capable of finding square, cube and squareroot of a number.


class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def cube(self):
        print(f"The value of {self.number} square is {self.number **3}")

    def squareroot(self):
        print(f"The value of {self.number} square is {self.number **0.5}")


a = calculator(9)
a.square()
a.cube()
a.squareroot()

# crate a class with a class attribute a; create an object from it and set a directly using object a=0. does this change the class attribute?


class sample:
    a = "harry"
    print(a)


obj = sample()
obj.a = "vicky"

# crate a to greet user with a message


class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def cube(self):
        print(f"The value of {self.number} square is {self.number **3}")

    def squareroot(self):
        print(f"The value of {self.number} square is {self.number **0.5}")

    @staticmethod
    def greet():
        print(
            "*********Hello there welcome to the best calculator of the world*********"
        )


a = calculator(9)
a.square()
a.cube()
a.squareroot()
a.greet()

# write a class train method to book a ticket , get status(no of seats), and get fare information of the train.

class train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
            print(
                f"the name of the train is {self.name} the seats available in the train is {self.seats} the fare of the train is {self.fare}"
            )

    def fareInfo(self):
            print(f"the fare of the train is {self.fare}")
    
    def booktikits(self):
        print(f"the seats available in the train is {self.seats}")
        if self.seats > 0:
            print(f"your seat is booked in the train {self.name} the fare of the train is {self.fare} the seats available in the train is {self.seats} ")
            self.seats = self.seats - 1
        else:
            print(f"no seats available in the train")
    
    def cancelTicket(self,seat):
        print(f"your ticket is cancelled the seat number is {seat}")
        self.seats = self.seats + 1
        

intercity = train("Intercity Express", 100, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.booktikits()
intercity.cancelTicket(1)

#  can you change the self parameter inside a class to something else (say "harry")? try changing self to "slf" or "harry" and see the effects.

class name :
    def __init__(slf,name):
        slf.name = name 
        print(slf.name)

obj = name("harry")

# you can  use the self parameter to anything else but it is not a good practice to use the self parameter to anything else.
# the self parameter is the reference to the object of the class.

