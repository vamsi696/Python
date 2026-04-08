nums = [10, 20, 30, 40, 50]
target = 30

for num in nums:
    if num == target:
        print("Found the target number:", num)
        break
else:
    print("Target number not found in the list.")
