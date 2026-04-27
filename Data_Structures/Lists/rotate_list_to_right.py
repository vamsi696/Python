lst = [1, 2, 3, 4, 5]
k = 1

k = k % len(lst)
rotated_lst = lst[-k:] + lst[:-k]
# slice and join
# lst = [1, 2, 3, 4, 5]
# k = 2
# lst[-2:]  →  [4, 5]     # from 2nd last to end
# lst[:-2]  →  [1, 2, 3]  # from start up to (not including) last 2
print("Rotated List:", rotated_lst)
