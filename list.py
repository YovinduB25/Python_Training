# Lists
"""Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used
to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets """

# List Items
"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

list = ["abc", 34, True, 40, "male", 40]

print(list)
print(len(list))
print(type(list))

# Creating a lsit with list constructor list()
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# List items are indexed and you can access them by referring to the index number

print(list[1])

# Negative indexing means start from the end
print(list[-1])

# rannge
print(list[2:5])

print(list[:4])
print(list[2:])

# changing the value
list[3] = 60
print(list)

# changing a range of value
list[0:1] = ["def", 43]
print(list)

list1 = ["apple", "banana", "cherry"]
list1[1:2] = ["blackcurrant", "watermelon"]
print(list1)

# adding to a list using append method
list1.append("orange")
print(list1)

# insert a list item at a specified index, use the insert() method.
list1.insert(0, "melon")
print(list1)

# To append elements from another list to the current list, use the extend() method.
list.extend(list1)
print(list)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
tuple = ("h3llo", "w0rls")
list.extend(tuple)
print(list)
