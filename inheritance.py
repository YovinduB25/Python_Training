# Python Inheritance
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""


# parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Yovindu", "Banula")
x.printname()


# child class
class Student1(Person):
    pass


y = Student1("Mason", "Mount")
y.printname()


# adding __init__ to child class
class Student2(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


# Here, this no longer inherits parent's class init(), instead of that now its overrides the init()
# The child's __init__() function overrides the inheritance of the parent's __init__() function.


# to keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student3(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Super Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class Student4(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # inherits all the properties from the parent class


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties
class Student5(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


x = Student5("Mike", "Olsen")
print(x.graduationyear)


# Adding year parameter
class Student6(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student6("Mike", "Olsen", 2023)
print(x.graduationyear)


# Add methods
class Student7(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student7("Mike", "Olsen", 2019)
x.welcome()
