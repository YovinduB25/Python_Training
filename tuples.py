# Tuples is a collection which is ordered and unchangeable. Uses () to define a tuple.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)

# Tuple items are ordered, unchangeable, and allow duplicate values. Tuple items are indexed.

# length
print(len(thistuple))
print(type(thistuple))

"""To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize 
it as a tuple. """

thistuple1 = ("apple",)  # use the comma
print(type(thistuple1))

# NOT a tuple
thistuple1 = ("apple")
print(type(thistuple1))

# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3, 5, 3, 7)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

# Accessing a tuple
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])  # index 5 (not included)
print(thistuple[:4])
print(thistuple[3:])
print(thistuple[-3:-1])

if "banana" in thistuple:
    print('yes, \'banana\' is in this tuple')

"""
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
"""
# Updating tuple
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ('abc', 'cde', 'efg','hij')
y = list(x)
y[1] = 'klm'
x = tuple(y)
print(x)

print('')

# Add items
# Method 1:
x1 = ("apple", "banana", "cherry")
y1 =list(x1)
y1.append('orange')
x1 = tuple(y1)
print(x1)

print('')
# Method 2: Add tuple to a tuple
x2 = ("apple", "banana", "cherry")
y2 = ("kiwi",)
x2 += y2
print(x2)

print('')
# Removing items
x3 = ("apple", "banana", "cherry")
y3 = list(x3)
y3.remove('apple')
x3 = tuple(y3)
print(x3)

# Deleting tuple
# del x3
# print(x3)   #this will raise an error because the tuple no longer exists

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect 
the remaining values as a list. """

print('')
# Using *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print('')
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print('')
# Looping
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print('')
# looping through index number
for i in range(len(thistuple)):
    print(thistuple[i])

print('')
# Using while loop
n = 0
while n < len(thistuple):
    print(thistuple[n])
    n += 1

print('')
# joining tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
tuple4 = tuple1 * 2
print(tuple4)

# Tuple Methods
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""