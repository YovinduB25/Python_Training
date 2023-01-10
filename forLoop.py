# For Loops
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in
other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

# lopping item in a list, tuple, set
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping strings
for x in 'banana':
    print(x)

# break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print()
# continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print()
# range()
"""To loop through a set of code a specified number of times, we can use the range() function, The range() function 
returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified 
number. """

for x in range(10):
    print(x)

print()
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by
# adding a parameter.
for x in range(4, 10):
    print(x)

print()
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value
# by adding a third parameter.
for x in range(1, 30, 3):
    print(x)

print()
# else
for x in range(3, 15):
    print(x)
else:
    print('3 is the starting number.')

# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

print()
# Nested Loops
# The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
for x in [1, 2, 3]:
    pass
