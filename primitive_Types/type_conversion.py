x = input("x: ")
print(type(x))  # type denotes which primitive type is being used

y = int(x) + 1
print(f"x: {x}, y: {y}")

# type conversion
# int
# float
# bool
# str

# In boolean we have falsy which is having default value as
# "" -> empty strings
# 0 -> zero is false
# None -> none is also considered as false value

print(bool("false"))  # returns true as it is filled with string value
print(bool(""))  # returns false as it's having empty strings
none = ""
print(bool(none))  # returns false as value is undefined
