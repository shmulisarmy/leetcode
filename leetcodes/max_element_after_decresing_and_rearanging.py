nums = [2, 7, 3, 2, 9]

nums.sort()

nums[0] = 1

for num_index in range(1, len(nums)):
    nums[num_index] = min(nums[num_index], nums[num_index -1] + 1)

print(nums)
