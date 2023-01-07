# Conditions
"""
Equal a == b
Not equal a != b
Less than a < b
Less than or equal a <= b
Greater than a > b
Greater than or equal a => b
"""

# if
a = 20
b = 323
if a < b:
    print('b is bigger than a')

# elif
# if the previous conditions were not true, then try this condition
c = 20
d = 20
if c > d:
    print('c is bigger than d')
elif c == d:
    print('c,d values are equal')

# else
# The else keyword catches anything which isn't caught by the preceding conditions.
e = 32
f = 45
if e > f:
    print('e is bigger than f')
elif e == b:
    print('e,f values are equal')
else:
    print('f is bigger than e')

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
g = 10
h = 11
if g < h: print('h is bigger than g')

# Short Hand If ... Else
i = 33
j = 44
print('I') if i > j else print('J')

# This technique is known as Ternary Operators, or Conditional Expressions.
k = 55
l = 55
print('k') if k > l else print('=') if k == l else print('l')

# And
# The and keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b and b < c:
    print('both conditions are true')

# Or
# The or keyword is a logical operator, and is used to combine conditional statements
if a > b or b > c:
    print('only one condition is right')

print()
# Nested If
# You can have if statements inside if statements, this is called nested if statements
x = 41

if x > 10:
    print('x is bigger than 10')
    if x > 20:
        print('x is bigger then 20')
    else:
        print('x is smaller than 20')

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 1
b = 2
if a < b:
    pass    # having an empty if statement like this, would raise an error without the pass statement
