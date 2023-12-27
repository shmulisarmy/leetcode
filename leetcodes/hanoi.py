def hanoi(start, end, num):
    other = 6 - (start + end)

    if num > 1:
        hanoi(start, other, num-1)

    print(f"moving from {start} to {end}")

    if num > 1:
        hanoi(other, end, num-1)

hanoi(1, 3, 4)