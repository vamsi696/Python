lst = [10, -2, 33, 10, 5, -7, 33, 8]

max_value = min_value = lst[0]

for num in lst:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("Maximum value:", max_value)
print("Minimum value:", min_value)
