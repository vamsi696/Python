message = "a"


def greet(name):
    message = "Hello"


def greet_user(name):
    # this is not recommended, but it allows us to modify the global variable. This is bad practice.
    global message
    message = "Hello, " + name


greet("Alice")
# This will print "a" because the message variable inside the greet function
print(message)
