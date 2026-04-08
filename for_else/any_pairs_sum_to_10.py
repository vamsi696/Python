nums = [2, 4, 6, 3]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 10:
            print("pair found:", nums[i], nums[j])
            break
    else:
        continue
    break
else:
    print("No pairs found that sum to 10.")
