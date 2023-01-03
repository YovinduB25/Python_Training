# Tuples is a collection which is ordered and unchangeable. Uses () to define a tuple.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple items are ordered, unchangeable, and allow duplicate values. Tuple items are indexed.

# length
print(len(thistuple))

"""To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize 
it as a tuple. """

thistuple = ("apple",) #use the comma
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)