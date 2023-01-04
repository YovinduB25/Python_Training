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

thisdict2 = dict(name = "John", age = 36, country = "Norway")
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
thisdict1.update({"year" : 2023})
print(thisdict1)