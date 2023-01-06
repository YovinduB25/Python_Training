# Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

"""
Dictionaries are used to store data values in key:value pairs and can be referred to by using the key name.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

print(thisdict)
print(thisdict['brand'])

thisdict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict1)
print(len(thisdict1))

# Creating dictionary through dict() constructor
thisdict2 = dict(name="John", age=36, country="Norway")
print(thisdict2)

# Access items
x = thisdict1['year']
print(x)

# get()
y = thisdict1.get('colors')
print(y)

# Get Keys
# The keys() method will return a list of all the keys in the dictionar
z = thisdict1.keys()
print(z)

# Get Values
# The values() method will return a list of all the values in the dictionary.
w = thisdict1.values()
print(w)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
v = thisdict1.items()
print(v)

# Check if Key Exists
if 'brand' in thisdict1:
    print('yes')

if 'fuel' in thisdict1:
    print('yes')
else:
    print('no')

# Change Values
thisdict1["year"] = 2022
print(thisdict1)

# update()
thisdict1.update({"year": 2023})
print(thisdict1)

# Adding items
thisdict1["model"] = "Car"
print(thisdict1)

# use update too
thisdict1.update({"Wheels": 4})
print(thisdict1)

# Removing Items
# pop()
thisdict1.pop("Wheels")
print(thisdict1)

# popitem() method removes the last inserted item
thisdict1.popitem()
print(thisdict1)

# del will delete a specific name
del thisdict1["colors"]
print(thisdict1)

# The del keyword can also delete the dictionary completely
print(thisdict)
del thisdict
# print(thisdict)

print()

# clear() empties the dictionary
print(thisdict2)
thisdict2.clear()
print(thisdict2)

print()
# looping a dictionary
for x in thisdict1:
    print(x)

print()
for x1 in thisdict1:
    print(thisdict1[x1])  # print values

print()
# can use values()
for x2 in thisdict1.values():
    print(x2)

print()
# can use keys()
for x3 in thisdict1.keys():
    print(x3)

print()
# looping keys and  values
for y, z in thisdict1.items():
    print(y, z)

# Copying a dictionary
# use copy()
mydict = thisdict1.copy()
print(mydict)

# can use dict() too to copy
mydict1 = dict(thisdict1)
print(mydict1)

print()

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

# Can create a dictionary with multiple dictionaries
phone1 = {"name": "apple",
          "year": 2007,
          "available": True}

phone2 = {"name": "samsung",
          "year": 2011,
          "available": True}

phone3 = {"name": "htc",
          "year": 2012,
          "available": False}

myphones = {
    "phone1": phone1,
    "phone2": phone2,
    "phone3": phone3,
}
print(myphones)

# Dictionary Methods
"""
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""