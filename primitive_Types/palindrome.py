import math

number = 151
reverse_number = 0

if number < 0:
    number = abs(number)

original_number = number

while original_number != 0:
    last_digit = original_number % 10
    reverse_number = reverse_number * 10 + last_digit
    original_number //= 10

if number == reverse_number:
    print("True")
else:
    print("False")
