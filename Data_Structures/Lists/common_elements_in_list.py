a = [1, 2, 3, 4,]
b = [3, 4, 5, 6]

common_elements = []

for num in a:
    if num in b:
        common_elements.append(num)
print(common_elements)
