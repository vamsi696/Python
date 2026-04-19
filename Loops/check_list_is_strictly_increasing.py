nums = [1, 3, 5, 7, 9]

for i in range(len(nums) - 1):
    if nums[i] >= nums[i + 1]:
        print("The list is not strictly increasing.")
        break
else:
    print("The list is strictly increasing.")
