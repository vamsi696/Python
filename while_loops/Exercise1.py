count = 0
for numbers in range(1, 10):

    if numbers % 2 == 0:
        print(numbers)
        count += 1
print(f"we have {count} even numbers")
