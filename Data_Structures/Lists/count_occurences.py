lst = [1, 2, 2, 3, 2, 4, 5]
target = 2
count = 0

for item in lst:
    if item == target:
        count += 1
print(f"The number {target} occurs {count} times in the list.")
