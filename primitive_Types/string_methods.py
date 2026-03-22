# String methods are built-in functions that can be used to manipulate and work with strings in python.
# Here are some commonly used string methods:

course = "   python programming"
print(course.upper())  # converts the string to uppercase
print(course.lower())  # converts the string to lowercase
print(course.title())  # converts the first character of each word to uppercase
# removes any leading and trailing whitespace from the string
print(course.strip())
# returns the index of the first occurrence of the substring "pro"
print(course.find("pro"))
print(course.replace("p", "j"))  # replaces "p" with "j"
# finds pro is there in string or not returns boolean value
print("pro" in course)
# verifies "swift" word in availble in the string or not returns boolean value
print("swift" not in course)
