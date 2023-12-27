import math

def is_happy(num):
    seen = []
    while True:
        hold_num = 0
        digits = str(num).split()
        for digit in digits:
            hold_num += math.sqrt(int(digit))
        if hold_num in seen:
            return False
        if hold_num == 1:
            return True
        seen.append(hold_num)

for i in range(10000000):
    if is_happy(i):
        print(i)