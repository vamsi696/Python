a = [1, 2, 3, 4,]
b = [3, 4, 5, 6]

uncommon_elements = []
for num in a:
    if num not in b:
        uncommon_elements.append(num)
for num in b:
    if num not in a:
        uncommon_elements.append(num)
print(uncommon_elements)
