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

# remove method
list.remove("watermelon")
print(list)

# pop method is using remove specified index
list.pop(0)
print(list)

list.pop()  # when you not specific the index, it will remove the last elements
print(list)

# del can also use for same purpose
del list[1]
print(list)

# del list_name can use to delete the entire list

# clear() methode empties the list, but list still remains & empties the content
list.clear()
print(list)

# Looping the list
thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(thislist)

print("")
# looping through index number
for i in range(len(thislist)):
    print(thislist[i])

# using a while loop
j = 0
while j < len(thislist):
    print(thislist)
    j += 1

# Looping Using List Comprehension
[print(x) for x in thislist]

# list comprehension exercises
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# doing the same with one code
newList1 = [y for y in fruits if "e" in y]
print(newList1)

# syntax to the above logic
# newlist = [expression 'for' item 'in' iterable 'if' condition == 'True']

newList2 = [z for z in fruits if z != "apple"]
print(newList2)
print('')

# Iterable
newList3 = [x for x in range(10)]
print(newList3)

newList3 = [x for x in range(10) if x < 5]
print(newList3)

# Expression
newList = [x.upper() for x in fruits]
print(newList)

# Set all values in the new list to 'hello':
newList = ['hello' for x in fruits]
print(newList)

print('')
# Sort List
# use sort()
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

# To sort descending, use the keyword argument reverse = True:
thislist1.sort(reverse=True)
print(thislist1)

thislist2.sort(reverse=True)
print(thislist2)


# customize your own function by using the keyword argument key = function

def func(n):
    return abs(n - 50)


thislist2.sort(key=func)
print(thislist2)

# sorting when there different cases
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()
print(thislist)

thislist.sort(key=str.lower)  # using str.lower
print(thislist)

# The reverse() method reverses the current sorting order of the elements.
thislist.reverse()
print(thislist)

print('')

# Copy a list
# use copy()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
# mylist1 = list(thislist)
# print(mylist1)

# Join Lists
# Can use arithmatic operators
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print('')
# can use for loops too
for x in list2:
    list1.append(x)

print(list1)

# can use the extend() method, which purpose is to add elements from one list to another list:
list1.extend(list2)
print(list1)

# List Methods
"""
append()	Adds an element at the end of the list
clear() 	Removes all the elements from the list
copy()	    Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""