import random
def find_target(target):
    p1 = 0
    p2 = len(nums)-1
    middle = None
    while True:
        if middle == (p1+p2)//2:
            print(f'cannot find {target} in numbers list')
            break
        middle = (p1+p2)//2
        if nums[middle] == target:
            print(f'{target} is at the {middle} index')
            break 
        elif nums[middle] > target:
            p2 = middle
        elif nums[middle] < target:
            p1 = middle

nums = [i for i in range(0, 51, 2)]

for i in range(100):
    find_target(i)