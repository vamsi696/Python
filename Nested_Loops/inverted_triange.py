num = 4

for i in range(num, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row
