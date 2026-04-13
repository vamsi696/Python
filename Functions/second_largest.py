def second_largest(num):
    if len(num) < 2:
        return None
    largest = second_largest = float('-inf')

    for n in num:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n != largest:
            second_largest = n
    # Handle case where all numbers are the same or only one number is present
    return second_largest if second_largest != float('-inf') else None


print(second_largest([10, 45, 67, 23, 89, 12]))
