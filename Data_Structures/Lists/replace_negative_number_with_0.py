lst = [10, -2, 33, 10, 5, -7, 33, 8]
modified_lst = []

for num in lst:
    if num < 0:
        modified_lst.append(0)
    else:
        modified_lst.append(num)

print(modified_lst)
