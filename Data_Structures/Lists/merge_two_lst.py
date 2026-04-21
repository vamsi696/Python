lst = [10, -2, 33, 10, 5, -7, 33, 8]
lst2 = [11, 12, 13]
merged_lst = []

for num in lst:
    merged_lst.append(num)
for num in lst2:
    merged_lst.append(num)

merged_lst.sort()
print(merged_lst)

unique_lst = []
for num in merged_lst:
    if num not in unique_lst:
        unique_lst.append(num)
print(unique_lst)
