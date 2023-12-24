stock_prices = [7, 1, 5, -6, 10, 4]

roi = lambda selling_point_index, buying_point_index: stock_prices[selling_point_index] - stock_prices[buying_point_index]
#loop starts off by incrementing
buying_point_index = 0
best_roi = 0

while buying_point_index < len(stock_prices)-1:
    print(f"{buying_point_index = }")
    print('stock =', stock_prices[buying_point_index])
    for selling_point_index in range(buying_point_index, len(stock_prices)):
        print('roi =',stock_prices[selling_point_index] - stock_prices[buying_point_index])
        best_roi = max(best_roi, roi(selling_point_index, buying_point_index))
        if stock_prices[selling_point_index] < stock_prices[buying_point_index]:
            buying_point_index = selling_point_index-1
            break

    buying_point_index += 1
            


print(best_roi)