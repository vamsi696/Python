arr = [1, 2, 3, 7, 8, 9]
# Find pairs in the array that sum to 10

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == 10:
            print(arr[i], arr[j])
