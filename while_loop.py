# Python Loops

# Python has two primitive loop commands:
# while loops
# for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
    print(i)
    i += 1

print()
# The break Statement
# With the break statement we can stop the loop even if the while condition is true
j = 1
while j < 10:
    print(j)
    if j == 8:
        break
    j += 1

print()
# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
k = 1
while k < 6:
    k += 1
    if k == 3:
        continue
    print(k)

print()
# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
l = 1
while l < 8:
    print(l)
    l += 1
else:
    print('l is no longer bigger than 8')