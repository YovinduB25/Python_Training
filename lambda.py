# Python Lambda
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments
x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(10, 20, 30))

"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
"""


def myfunc(n):
    return lambda a: a * n


double = myfunc(2)  # Use that function definition to make a function that always doubles the number you send in
print(double(11))

thrible = myfunc(3)
print(thrible(11))

# Use lambda functions when an anonymous function is required for a short period of time.