s = "aabbccdeef"
count_unique = 0

for ch in s:
    if s.count(ch) == 1:
        count_unique += 1
        if count_unique == 2:
            print("Second non-repeating character:", ch)
            break
else:
    if count_unique < 2:
        print("Second non-repeating character not found.")
