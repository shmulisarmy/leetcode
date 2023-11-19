from functools import cache

@cache
def give_change(target):
    smallest_coin_amount = 10
    for coin in coins:
        if coin <= target:
            if coin == target:
                change_amount = 1
            else:
                newTarget = target - coin
                change_amount = give_change(newTarget) + 1

            smallest_coin_amount = min(smallest_coin_amount, change_amount)

    return smallest_coin_amount

coins = [1, 4, 7]

print(give_change(14))