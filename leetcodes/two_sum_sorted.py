


def find_three_sum(target, list, i):
    third = list.pop(i)
    target -= third
    p1 = 0
    p2 = len(list) -1
    while list[p1] + list[p2] != target:
        if list[p1] + list[p2] < target:
            p1 += 1
        if list[p1] + list[p2] > target:
            p2 -= 1
        if p1 == p2:
            return -1


    return (list[p1], list[p2], third)

nums = [1, 3, 4, 5, 7, 8, 9]
for i in range(len(nums)):
    print(find_three_sum(20, [i for i in nums], i))