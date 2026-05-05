lst = [1, 2, 3, 4, 5]
k = 2
k = k % len(lst)

left_rotated_lst = lst[k:] + lst[:k]
# slice and join
# lst = [1, 2, 3, 4, 5]
# k = 2
# lst[2:]  →  [3, 4, 5]  # from index 2 to end
# lst[:2]  →  [1, 2]     # from start up to (not including) index 2

print("Left Rotated List:", left_rotated_lst)
