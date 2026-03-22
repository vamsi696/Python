# variables that are created outside of a function is known as Global variables

x = "awesome"


def myfunc():
    print("Python is" + x)


myfunc()

y = "awesome"


def myfirstfunc():
    y = "fantastic"
    print("python is" + y)


myfirstfunc()
print("python is" + y)

# If you use global keyword, the variable belongs to the global scope
z = "super"


def myfunc():
    global z
    z = "cool"


myfunc()
print("python is " + z)
