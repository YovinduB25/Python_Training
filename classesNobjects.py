# Python Classes/Objects
"""
Python is an object-oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""


class myClass:
    x = 5


print(myClass)

# Create Object
c1 = myClass
print(c1.x)

# The __init__() Function
"""
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when 
the object is being created """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('John', 25)
print(p1.name)
print(p1.age)
print(p1)  # without the __str__()

print()
# The __str__() Function
"""
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned
"""


class Car:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.name}({self.date})"


car1 = Car("bmw", 2022)
print(car1)

print()


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("This animal is a " + self.name)


a1 = Animal("Dog", 4)
a1.myFunc()

print()

# The self Parameter
"""The self parameter is a reference to the current instance of the class, and is used to access variables that 
belongs to the class. 

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any 
function in the class """


# Use the words myobject and abc instead of self

class Maths:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def func(abc):
        print("Hell0!, my name is " + abc.name)


m1 = Maths("Banula", 23)
m1.func()

# Modify Object Properties
m1.age = 29
print(m1.age)

# Delete Object Properties
del m1.age
# print(m1.age)

# Delete Objects
del m1
# print(m1)

# The pass Statement
"""class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the 
pass statement to avoid getting an error. """


class Hello:
    pass

# having an empty class definition like this, would raise an error without the pass statement
