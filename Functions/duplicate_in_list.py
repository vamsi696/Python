def remove_duplicates(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))
