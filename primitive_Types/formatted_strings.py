# Formatted Strings is a string literal prefixed with 'f' or 'F' .
# 'f' string allows us to embed expressions , variables and functions directly inside the string using curly braces {}.

first_name = "Hemanth"
last_name = "Kandalla"
full_name = first_name + " " + last_name
print(full_name)  # prints Hemanth Kandalla

# Using formatted string
full_name1 = f"{first_name} {last_name}"
print(full_name1)  # prints Hemanth Kandalla

full_name2 = f"{len(first_name)} {last_name}"
print(full_name2)  # prints 7 Kandalla

full_name3 = f"{first_name.upper()} {last_name.lower()}"
print(full_name3)  # prints HEMANTH kandalla

full_name4 = f"{len(first_name)} {2 + 3}"
print(full_name4)  # prints 7 5

full_name5 = f"{first_name} {last_name} is a Python Developer"
print(full_name5)  # prints Hemanth Kandalla is a Python Developer

full_name6 = f"{first_name[2]} {last_name[1]}"
print(full_name6)  # prints m a

full_name7 = f"{first_name} {last_name} is a Python Developer and his name has {len(first_name) + len(last_name)} characters"
# prints Hemanth Kandalla is a Python Developer and his name has 15 characters
print(full_name7)
