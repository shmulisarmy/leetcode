def main(nums):
    l1 = []
    l2 = []
    temp = 1
    for i, n in enumerate(nums):
        l1.append(temp)
        temp *= n
    temp = 1
    for i in range(len(nums)-1, -1, -1):
        l2.append(temp)
        temp *= nums[i]


    return [l1[i]*l2[-i-1] for i in range(len(nums))]

print(main(range(1, 6)))