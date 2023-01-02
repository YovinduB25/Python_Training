# Strings are arrays
a = 'Hello Banula'
print(a[1])  # e will be the result since array stats from 0
print(len(a))  # len() function use to check the length

for x in 'banula':
    print(x)

# check sting
txt = "The best things in life are free!"
print("free" in txt)

# using a string
text = "The best things in life are free!"
if 'best' in text:
    print('best is in the text')

# check if not
# using not in
txt1 = "The best things in life are free!"
print("expensive" not in txt1)

txt2 = "The best things in life are free!"
if "expensive" not in txt2:
    print("No, 'expensive' is NOT present.")

# Slicing
"""You can return a range of characters by using the slice syntax."""
print(txt2[3:23])
print(txt2[:23])  # slicing from the start
print(txt2[3:])  # slicing from the end

# negative indexing
b = 'hello world'
print(b[-5:-2])

# Modify String

c = 'Hello Chelsea!'
print(c.upper())
print(c.lower())
print(c.strip())  # remove white space
print(c.replace("H", "J"))  # replacing string
print(c.split(","))  # returns a list where the text between the specified separator becomes the list items.
print(c.split("C"))
print(c.split("s"))

# String concatenation
print(b + c)
print(b + " " + c)

# format() can pass values in to string where placeholder is {}

d = 22
e = 'I am {} years old'
print(e.format(d))

quantity = 3
itemno = 567
price = 49.95
myOrder1 = 'I want {} pieces of item {} for {} dollars.'
print(myOrder1.format(quantity, itemno, price))

myOrder2 = "I want to pay {2} dollars for {0} pieces of item {1}."  # We can use indexing
print(myOrder2.format(quantity, itemno, price))

# Escape Characters
"""
\'	Single Quote #uses when use single quotes	
\\	Backslash	#use to put backlash
\n	New Line	#use for a new line
\r	Carriage Return     #use to split words in to 2 lines
\t	Tab	    #use to put a tab
\b	Backspace	use to backspace
\f	Form Feed	
"""
# \000 use to octal values
# \xhh use to hex values

txt3 = "Hello this is \"Vikings\" from the north"
print(txt3)

# https://www.w3schools.com/python/python_strings_methods.asp Check the String Methods
