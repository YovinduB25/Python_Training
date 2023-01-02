# bool() can use to evaluate values
print(bool(15))

"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

print(bool("abc"))
print(bool(""))

print(bool(123))
print(bool(0))

print(bool(["apple", "cherry", "banana"]))
print(bool([]))
print(bool(None))


class myClass():  # Here also value will br false since value returns 0. This can happen with returning value with False
    def __len__(self):
        return 0


myObj = myClass()
print(bool(myObj))


# Can create functions that return boolean
def myfunc():
    return True


print(myfunc())

"""Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be 
used to determine if an object is of a certain data type: """

x = 200
print(isinstance(x,int))
print(isinstance(x,str))