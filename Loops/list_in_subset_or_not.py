a = [1, 2]
b = [1, 2, 3, 4]

for x in a:
    if x not in b:
        print(f"{x} is not in list b.")
        break
else:
    print(f"All elements of list a {a} are in list b {b}.")
