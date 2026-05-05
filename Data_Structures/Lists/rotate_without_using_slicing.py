def rotate_right(arr, k):
    k = k % len(arr)  # Handle cases where k is greater than array length

    for _ in range(k):
        last_element = arr[-1]  # Store the last element
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]  # Shift elements to the right
        arr[0] = last_element  # Place the last element at the front
    return arr


print(rotate_right([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
