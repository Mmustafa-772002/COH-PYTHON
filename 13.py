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
    location = "delhi"

    def changeSalary(self, sal):
        self.salary = sal


e = employee()
print(e.salary)
print(e.location)
e.changeSalary(200)
print(e.salary)

# hierarchical inheritance : when a class is inherited by multiple classes then it is called hierarchical inheritance

# TODO : add example of hierarchical inheritance -- done


# Define the Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


# Define the Dog class, which inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


# Define the Cat class, which inherits from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")


# Define the Labrador class, which inherits from Dog
class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} is fetching.")


# Create an instance of the Dog class
dog = Dog("Buddy")
dog.eat()  # Call the eat method of the Animal class
dog.bark()  # Call the bark method of the Dog class

# Create an instance of the Cat class
cat = Cat("Whiskers")
cat.eat()  # Call the eat method of the Animal class
cat.meow()  # Call the meow method of the Cat class

# Create an instance of the Labrador class
labrador = Labrador("Max")
labrador.eat()  # Call the eat method of the Animal class
labrador.bark()  # Call the bark method of the Dog class
labrador.fetch()  # Call the fetch method of the Labrador class


# hybrid inheritance : when a class is inherited by multiple classes and those classes are inherited by other classes then it is called hybrid inheritance


# Define the Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


# Define the Dog class, which inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


# Define the Cat class, which inherits from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")


# Define the Labrador class, which inherits from Dog
class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} is fetching")


# Create an instance of the Dog class
dog = Dog("Buddy")
dog.eat()  # Call the eat method of the Animal class
dog.bark()  # Call the bark method of the Dog class

# Create an instance of the Cat class
cat = Cat("Whiskers")
cat.eat()  # Call the eat method of the Animal class
cat.meow()  # Call the meow method of the Cat class

# Create an instance of the Labrador class
labrador = Labrador("Max")
labrador.eat()  # Call the eat method of the Animal class
labrador.bark()  # Call the bark method of the Dog class
labrador.fetch()  # Call the fetch method of the Labrador class


# method overloading : Method overloading is a feature that allows a class to have more than one method having the same name, if their argument lists are different. It is similar to constructor overloading in Java.


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("let's multiply")
        return self.num * num2.num


n1 = Number(2)
n2 = Number(8)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
# operator in the python are overloaded by using the dunder methods

# operator can be overloaded using following dunder methods
# p1 + p2  => p1.__add__(p2)
# p1 - p2  => p1.__sub__(p2)
# p1 * p2  => p1.__mul__(p2)
# p1 / p2  => p1.__div__(p2)
# p1 // p2  => p1.__floordiv__(p2)
# p1 % p2  => p1.__mod__(p2)
# p1 ** p2  => p1.__pow__(p2)
# p1 += p2  => p1.__iadd__(p2)
# p1 -= p2  => p1.__isub__(p2)
# p1 *= p2  => p1.__imul__(p2)
# p1 /= p2  => p1.__idiv__(p2)
# p1 //= p2  => p1.__ifloordiv__(p2)
# p1 %= p2  => p1.__imod__(p2)
# p1 **= p2  => p1.__ipow__(p2)
# p1 == p2  => p1.__eq__(p2)


# other magic methods
#   __str__() : returns string
# example :
class employee:
    company = "google"
    salary = 100

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"


e = employee()
e.name = "Rohan"
print(e)

# __rep__() : returns string
# example :


class employee:
    company = "google"
    salary = 100

    def __repr__(self):
        return f"The name is {self.name} and salary is {self.salary}"


e = employee()
e.name = "Rohan"
print(e)

# __len__() : returns length of the object
# example :


class employee:
    company = "google"
    salary = 100

    def __len__(self):
        return len(self.name)


e = employee()
e.name = "Rohan"
print(len(e))

# __getitem__() : returns the item of the object
# example :


class employee:
    company = "google"
    salary = 100

    def __getitem__(self, index):
        return self.name[index]


e = employee()
e.name = "Rohan"
print(e[1])


# __setitem__() : sets the item of the object
# # example :
class employee:
    company = "google"
    salary = 100

    def __setitem__(self, index, value):
        self.name = list(self.name)
        self.name[index] = value
        self.name = "".join(self.name)


e = employee()
e.name = "Rohan"
e[1] = "s"
print(e.name)

# TODO : fix the above code to work correctly  -- done


# __delitem__() : deletes the item of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __delitem__(self, index):
        self.name = self.name[:index] + self.name[index + 1 :]


e = employee()
e.name = "Rohan"
del e[1]
print(e.name)


# __contains__() : returns true if the item is present in the object
# example :
class employee:
    company = "google"
    salary = 100

    def __contains__(self, value):
        return value in self.name


e = employee()
e.name = "Rohan"
print("R" in e)


# __call__() : calls the object
# example :
class employee:
    company = "google"
    salary = 100

    def __call__(self):
        return "This is a callable object"


e = employee()
print(e())


# __iter__() : returns the iterator object
# example :
class employee:
    company = "google"
    salary = 100

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x < 5:
            self.x += 1
            return self.x
        else:
            raise StopIteration


e = employee()
for i in e:
    print(i)


# __next__() : returns the next item in the iterator
# example :
class employee:
    company = "google"
    salary = 100

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x < 5:
            self.x += 1
            return self.x
        else:
            raise StopIteration


e = employee()
for i in e:
    print(i)


# __add__() : returns the addition of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __add__(self, other):
        return self.salary + other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1 + e2)


# __sub__() : returns the subtraction of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __sub__(self, other):
        return self.salary - other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1 - e2)


# __mul__() : returns the multiplication of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __mul__(self, other):
        return self.salary * other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1 * e2)


# __truediv__() : returns the division of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __truediv__(self, other):
        return self.salary / other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1 / e2)


# __floordiv__() : returns the floor division of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __floordiv__(self, other):
        return self.salary // other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1 // e2)


# __mod__() : returns the modulus of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __mod__(self, other):
        return self.salary % other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1 % e2)


# __pow__() : returns the power of the object
# example :
class employee:
    company = "google"
    salary = 100

    def __pow__(self, other):
        return self.salary**other.salary


e1 = employee()
e2 = employee()
e1.salary = 100
e2.salary = 200
print(e1**e2)

# create a class c-2d vector and use it to create another class c-3d vector


class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)

#  for more details go to python official documentation of data model

# create a class pet from a class animals and further create a class dog from pet class add the method bark to the dog class


class animal:
    animalType = "Mammal"


class pet:
    color = "white"


class dog:
    @staticmethod
    def bark():
        print("bow bow !!")


d = dog()
d.bark()

# multilevel inheritance

# create a class employee and add salary and increment properties to it. write a method salaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary value as given below.


class employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai / self.salary


e = employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2000
print(e.increment)

# decorators : A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate. In this tutorial, you'll learn how you can create decorators and how to use them. Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

#  write a class complex to represent complex numbers, along overloaded operators +, -, and * which adds, subtracts, and multiplies complex numbers respectively.


# Define a class Complex to represent complex numbers
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    # Overload the addition operator (+) to add two complex numbers
    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    # Overload the multiplication operator (*) to multiply two complex numbers
    def __mul__(self, c):
        return Complex(
            self.real * c.real - self.imaginary * c.imaginary,
            self.real * c.imaginary + self.imaginary * c.real,
        )

    # Override the string representation of the complex number
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# Create two complex numbers
c1 = Complex(1, 4)
c2 = Complex(3, 4)

# Perform addition and multiplication of complex numbers
print(c1 + c2)
print(c1 * c2)

# write a class vector representing a vector of n dimension. overload the + and * operator which calculates the sum and dot product of them.


class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1
        return str1[:-1]

    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1 = vector([1, 4, 6])
v2 = vector([1, 6, 9])
print(v1)
print(v1+v2)
print(v1)
print(v1*v2)

# method overriding : Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its parent class. When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

# Define the parent class
class Shape:
    def area(self):
        pass

# Define the child class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # Override the area method
    def area(self):
        return self.length * self.width

# Create an instance of the Rectangle class
rect = Rectangle(5, 3)
print(rect.area())  # Output: 15


# ----------------------------------------END----------------------------------------------