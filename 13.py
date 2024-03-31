# inheritances and more about the oops
# 1. Inheritance : Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly the existing class is a base class (or parent class).
# syntax : class derived_class_name(base_class_name):
# class employee: (this is the parent class)
#    code

# class programmer(employee):   (this is child class of employee)
#    code

# the child class can access the properties of parent class
# dry principle : dont repeat yourself
# Here are some key features of inheritance:


# A child class inherits all the attributes and methods of its parent class. This means that you can create a new class without having to rewrite the code for existing functionality.
# A child class can modify the behavior of its parent class by overriding its methods or adding new ones. This allows you to add new functionality to a class while still reusing existing code.
# A child class can also add new attributes and methods that are not present in its parent class. This allows you to extend the functionality of an existing class without modifying its code.
# Inheritance can be used to create a hierarchy of classes that share common behavior. For example, you might have a Vehicle class as the parent class, and then create child classes like Car, Truck, and Motorcycle that inherit from it.
# Inheritance can help to make your code more organized and modular. By defining separate classes for different types of objects, you can keep related code together and make it easier to reuse and modify.
class employee:
    company = "google"

    def showDetails(self):
        print("This is an employee")

    def getCountry(self, country="India"):

        print(f"The country is {country}")


class programmer(employee):
    language = "python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def getName(self, name):
        print(f"The name is {name}")


e = employee()
e.showDetails()
p = programmer()
p.getLanguage()
print(p.company)
f = employee()
f.getCountry()

# types of inheritance:
# single inheritance : when a class inherits only one class then it is called single inheritance (as shown above) the programmer class is inherited by employee class only once so it is single inheritance
# 1. single inheritance - one parent and one child


class employee:
    company = "google"

    def showDetails(self):
        print("This is an employee")

    def getCountry(self, country="India"):

        print(f"The country is {country}")


# multiple inheritance : when a class inherits multiple classes then it is called multiple inheritance (as shown below)
# 2. multiple inheritance - multiple parent and one child


class employee:
    company = "google"


class Freelancer:
    company = "facebook"
    level = 2

    def upGradelevel(self):
        self.level = self.level + 1


class programmer(employee, Freelancer):
    name = "Rohan"


p = programmer()
p.upGradelevel()
print(p.level)
print(p.company)


# multilevel inheritance : when a class inherits a class and that class inherits another class then it is called multilevel inheritance (as shown below)
# 3. multilevel inheritance - one parent and one child and that child is parent of another child class

class person:
    country = "India"

    def takeBreak(self):
        print("I am taking break")


class employee:
    company = "honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an employee so I am taking break")


class programmer(person, employee):
    company = "fiver"

    def getSalary(self):
        print(f"no Salary to programmer")


p = person()
p = employee()
p = programmer()
p.takeBreak()
print(p.country)
p.getSalary()
e = programmer()
p.getSalary()

pr = employee()
p.takeBreak()

# super() method : The super() method is used to call the parent class constructor. It is used to call the constructor of the parent class and to access the parent class methods and properties.
# super() method is used to call the parent class constructor
# super() method is used to call the parent class methods and properties


class person:
    country = "India"
    def __init__(self):
        print("in init of person")
    

    def takeBreak(self):
        print("I am taking break")

class employee(person):
    company = "honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        super().__init__()
        print("initializing employee class")
        # super class method is called here
        print("I am an employee so I am taking break")


e = employee()
e.takeBreak()

# static method : A static method is a method that belongs to the class rather than any object of the class. It is a method that is bound to the class and not the object of the class.
# class method : A class method is a method that is bound to the class rather than the object of the class. It is a method that is called on the class rather than the object of the class.
# class method is used when we want to access the class variable in the method

class employee:
    company = "google"
    salary = 100
    location= "delhi"
    
    def changeSalary(self,sal):
        self.salary = sal
    
e = employee()
print(e.salary)
print(e.location)
e.changeSalary(200)
print(e.salary)


# hierarchical inheritance : when a class is inherited by multiple classes then it is called hierarchical inheritance
# hybrid inheritance : when a class is inherited by multiple classes and those classes are inherited by other classes then it is called hybrid inheritance
