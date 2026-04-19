data = [1, 2, 3, 5, "a", 6]

for item in data:
    if not isinstance(item, int):
        print("Not all elements are integers.")
        break
else:
    print("All elements are integers.")
