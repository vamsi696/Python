lst = [1, 2, 3, 4, 5]
rev = []

for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])
print(rev)


lst.reverse()
print(lst)

# Using slicing
rev_slicing = lst[::-1]
print(rev_slicing)
