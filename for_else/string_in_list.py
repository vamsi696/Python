names = ["Alice", "Bob", "Charlie"]
search_name = "David"

for name in names:
    if name == search_name:
        print("Found the name:", name)
        break
else:
    print("Name not found in the list.")
