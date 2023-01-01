x = 'World'  # Variables are containers for storing data values.


def func1():
    x = 'Girl'
    print('This is a beautiful ' + x)


func1()
print('This is a beautiful ' + x)


# Using the global key word

def func2():
    global y  # making y as a global variable
    y = 20
    print(10 + y)


func2()
print(30 + y)
