def divisible_by_3_and_5_in_range(start, end):
    results = []
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            results.append(num)
    return results


print(divisible_by_3_and_5_in_range(1, 100))
