num = 4

for i in range(num):
    for j in range(num):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
