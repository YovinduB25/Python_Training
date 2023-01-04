# sets
myset = {"apple", "banana", "cherry"}

# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will appear.

print(myset)
# Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print(len(myset))
print(type(myset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1)
print(set2)
print(set3)
print(set4)

# set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print('')
# Access set items
# You cannot access items in a set by referring to an index or a key. you can yse a for loop

for x in myset:
    print(x)

print('banana' in myset)

print('')
# Adding to set
thisset = {"apple", "banana", "cherry"}
thisset.add('orange')
print(thisset)

# To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "melon"]
thisset.update(mylist)
print(thisset)

# remove items
# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove('melon')
thisset.discard('orange')
print(thisset)
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
print('')
"""
You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
"""

x = thisset.pop()
print(x)
print(thisset)

print()
# clear()
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #this will raise an error because the set no longer exists

print()
# loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print()
# Join sets
# can use union() and update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print()

set3 = set1.update(set2)
print(set3)

# Both union() and update() will exclude any duplicate items.
print()
# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

z = x.intersection(y)
print(z)

print()
# Keep All, But NOT the Duplicates
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
# use symmetric_difference_update()
x1.symmetric_difference_update(y1)
print(x)

print()
# symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
z1 = x1.symmetric_difference(y1)
print(z1)

"""
add()	                            Adds an element to the set
clear()	                            Removes all the elements from the set
copy()	                            Returns a copy of the set
difference()	                    Returns a set containing the difference between two or more sets
difference_update()	                Removes the items in this set that are also included in another, specified set
discard()	                        Remove the specified item
intersection()	                    Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                    Returns whether two sets have a intersection or not
issubset()	                        Returns whether another set contains this set or not
issuperset()	                    Returns whether this set contains another set or not
pop()	                            Removes an element from the set
remove()	                        Removes the specified element
symmetric_difference()	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    inserts the symmetric differences from this set and another
union()	                            Return a set containing the union of sets
update()	                        Update the set with the union of this set and others
"""
