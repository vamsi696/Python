numbers = [10, 45, 67, 23, 89, 12]
# inf stand for negative infinity which is the smallest possible value
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The second largest number is:", second_largest)
