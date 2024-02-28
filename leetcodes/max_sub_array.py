nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_seq = 0
cur_seq = 0
found = None
i = 0
while i < len(nums):
    cur_seq = 0
    for j in range(i, len(nums)):
        cur_seq += nums[j]
        if cur_seq < 1:
            i = j
        
            break
        if cur_seq > max_seq:
            max_seq = cur_seq
            found = (i, j)
    i += 1


print(max_seq, found)