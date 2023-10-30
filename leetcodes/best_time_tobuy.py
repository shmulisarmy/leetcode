stocks = [7, 1, 3, 6, 5]


big = 0
for i in range(len(stocks)):
    for j in range(i + 1, len(stocks)):
        if stocks[j] <= stocks[i]:
            break
        big = max(big, stocks[j] - stocks[i]) 

print(big)