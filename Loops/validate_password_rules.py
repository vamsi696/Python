import string

password = "Test@123"

has_upper = has_lower = has_digit = has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in string.punctuation:
        has_special = True

if has_upper and has_lower and has_digit and has_special:
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")
