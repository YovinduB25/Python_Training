# Python Arrays
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable

cars = ['bmw', 'benz', 'ford']

# An array can hold many values under a single name, and you can access the values by referring to an index number.
# accessing array
x = cars[0]
print(x)

# modifiying
cars[0] = 'toyota'
print(cars)

# length
print(len(cars))

# The length of an array is always one more than the highest array index.
# looping
for x in cars:
    print(x)

# adding
cars.append('honda')
print(cars)

# pop
cars.pop(1)
print(cars)

cars.remove('ford')
print(cars)

"""
Array Methods
Python has a set of built-in methods that you can use on lists/arrays.

Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""