from collections import defaultdict

bigest = 0

numbers_seen = []
numbers = [100, 4, 5, 200, 1, 2, 3]

def next_number(num):
    numbers_seen.append(num)
    if num + 1 in numbers:
        return 1 + next_number(num +1)

    return 1

for  num in numbers:
    if num in numbers_seen: continue
    print(f'sequence from {num} goes all the way to {num + next_number(num) -1}')

#time colmexity is log(n) 
# #becuase whenever a recursion is called it puts that the bigger number is numbers seen so it gets skiped 
# #(and that also deals with duplicates)