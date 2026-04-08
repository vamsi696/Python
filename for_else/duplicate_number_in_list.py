num = [1, 2, 3, 4, 5, 2, 1, 6]
seen = set()

for n in num:
    if n in seen:
        print("Duplicate number found:", n)
        break
    seen.add(n)
else:
    print("No duplicate numbers found in the list.")
