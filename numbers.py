# Numbers
"""
int = Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
Ex: x = 1
    y = 35656222554887711
    z = -3255522

float = Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Ex: x = 1.10
    y = 1.0
    z = -35.59

    # Float can also be scientific numbers with an "e" to indicate the power of 10.
    x = 35e3
    y = 12E4
    z = -87.7e100


complex = Complex numbers are written with a "j" as the imaginary part:
Ex: x = 3+5j
    y = 5j
    z = -5j
"""

# Type conversion can be done using type()
x = 1.43
x = int(x)
print(x, type(x))
x = complex(x)
print(x, type(x))

# Random Numbers
"""Python does not have a random() function to make a random number, but Python has a built-in module called random 
that can be used to make random numbers: """

import random

print(random.randrange(1, 10))
