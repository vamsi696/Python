import math

number = -123

digit = 0

if number < 0:
    number = (abs(number))

while number != 0:
    total_Count = number % 10
    digit = digit + total_Count
    number //= 10

print(digit)
