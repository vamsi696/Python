import math

number = -1234

reverse_Number = 0

if number < 0:
    number = (abs(number))

while number != 0:
    last_Digit = number % 10
    reverse_Number = reverse_Number * 10 + last_Digit
    number //= 10

print(reverse_Number)
