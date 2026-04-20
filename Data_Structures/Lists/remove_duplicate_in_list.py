lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)  # append the unique item to the new list
print(unique_lst)
