def find_Largest(num):
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    return largest


print(find_Largest([45, 67, 82, 23, 99, 56]))
