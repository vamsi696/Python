def findSmallest(num):
    smallest = num[0]
    for i in num:
        if i < smallest:
            smallest = i
    return smallest


print(findSmallest([45, 67, 82, 23, 99, 56]))
