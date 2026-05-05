def rotate_left(arr, k):
    k = k % len(arr)  # Handle cases where k is greater than array length

    for _ in range(k):
        first_element = arr[0]  # store the first element
        for i in range(0, len(arr) - 1):
            arr[i] = arr[i + 1]  # shift elements to the left
        arr[-1] = first_element  # place the first element at the end
    return arr


print(rotate_left([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]
