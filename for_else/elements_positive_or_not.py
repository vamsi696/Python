num = [2, 4, 6, -1, 8]

for n in num:
    if n < 0:
        print("Negative number found:", n)
        break
else:
    print("All numbers are positive.")
