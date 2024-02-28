buiildings = [20,7,6,30,8,2,10]

left_biggest = []
right_biggest = []

left_max_so_far = 0
right_max_so_far = 0

for i in range(len(buiildings)):
    left_max_so_far = max(left_max_so_far, buiildings[i])
    left_biggest.append(left_max_so_far)
    right_max_so_far = max(right_max_so_far, buiildings[-i-1])
    right_biggest.append(right_max_so_far)


for i in range(len(left_biggest)):
    buiildings[i] = max(min(left_biggest[i], right_biggest[-i-1]), buiildings[i])

print(buiildings)
    

