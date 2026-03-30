numbers = [10, 45, 32, 67, 5]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
print("The largest number in the list is:", largest)
