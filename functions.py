# Functions
"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""


# In Python a function is defined using the def keyword:
def func():
    print('hello there!')


func()

""""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want,
just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name,
which is used inside the function to print the full name:
"""


def my_func(fname):
    print(fname + " refense")


my_func("Emails")
my_func("Linus")
my_func("Words")

"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emails", "Refsnes")

print()
# Arbitrary Arguments, *args
"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name 
in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""


def function(*kids):
    print("The youngest child is " + kids[2])


function("Emil", "Tobias", "Linus")

print()


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function1(child3, child2, child1):
    print("The youngest child is " + child3)
    print("The eldest child is" + child1)
    print("Sa hi to, " + child2)


my_function1(child1="Emil", child2="Tobias", child3="Linus")

# Keyword Arguments are often shortened to kwargs in Python documentations.

print()
# Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the
parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""


def my_func1(**kid):
    print("His last name is " + kid["lname"])


my_func1(fname="Tobias", lname="Refsnes")

print()


# Default Parameter Value
def my_function2(country="Norway"):
    print("I am from " + country)


my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")

print()
# Passing a List as an Argument
"""
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated
as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function
"""


def my_function3(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function3(fruits)

print()


# Return Values
# To let a function return a value, use the return statement
def my_function4(x):
    return 5 * x


print(my_function4(3))
print(my_function4(5))
print(my_function4(9))


# pass
def myfunction5():
    pass


# having an empty function definition like this, would raise an error without the pass statement

print()
# Recursion
"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the 
benefit of meaning that you can loop through data to reach a result. 

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which 
never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly 
recursion can be a very efficient and mathematically-elegant approach to programming. 

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable 
as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 
(i.e. when it is 0). 

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and 
modifying it. """


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
