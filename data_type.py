""" Data Types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

All the data types in python is here"""

a = range(6)
print(a, type(a))

b = ["apple", "banana", "cherry"]  # list
print(b, type(b))

c = ("apple", "banana", "cherry")  # tuple
print(c, type(c))

d = 3j  # complex
print(d, type(d))

e = {"name": "Banula", "age": 22}  # dictionary
print(e, type(e))

f = {"apple", "banana", "cherry"}  # set
print(f, type(f))

g = frozenset({"apple", "banana", "cherry"})  # Frozen set
print(g, type(g))
"""Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any 
time, elements of the frozen set remain the same after creation. Due to this, frozen sets can be used as keys in 
Dictionary or as elements of another set. """

h = b"hello"  # bytes
print(h, type(h))

i = bytearray(5)  # byte array
print(i, type(i))
"""
A consecutive sequence of variables of the data type byte.
bytearray() method returns a bytearray object which is an array of given bytes. It gives a mutable sequence of 
integers in the range 0 <= x < 256. """

j = memoryview(bytes(12))  # memory array
print(j, type(j))

"""memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol 
without copying. The memoryview() function allows direct read and write access to an object's byte-oriented data 
without needing to copy it first. """
