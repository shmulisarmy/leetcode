"""dynamic programming solution that has a time complexity of o(n*n) and memory of o(n)"""
coins = [1,3,4,5]

change = 7

coins_needed = dict()

for i in range(1, change + 1):
    if i in coins:
        coins_needed[i] = 1
    else:
        coins_for_cur = None
        for j in coins_needed:
            if coins_for_cur == None or coins_for_cur > coins_needed[j] + coins_needed[i - j]:
                coins_for_cur = coins_needed[j] + coins_needed[i - j]
        if coins_for_cur:
            coins_needed[i] = coins_for_cur

print(coins_needed[change])