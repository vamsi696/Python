a = [1, 2, 3]
b = [6, 4, 5]

for x in a:
    if x in b:
        print(f"Common element found: {x}")
        break
else:
    print("No common element found.")
