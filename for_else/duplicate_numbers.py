nums = [1, 2, 3, 4, 5, 2, 1, 6]
seen = set()
duplicates = set()

for n in nums:
    if n in seen:
        duplicates.add(n)
    seen.add(n)
else:
    if duplicates:
        print("Duplicate numbers found:", duplicates)
    else:
        print("No duplicate numbers found in the list.")
