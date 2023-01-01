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
print(txt2[3:])   # slicing from the end

#negative indexing
b = 'hello world'
print(b[-5:-2])

