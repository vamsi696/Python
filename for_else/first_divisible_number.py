nums = [3, 5, 11, 13, 21]

for num in nums:
    if num % 7 == 0:
        print("First number divisible by 7 is:", num)
        break
else:
    print("No number is divisible by 7 in the list.")
