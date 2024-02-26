collection_of_items = input().split("|")
budget = float(input())

list_new_prices = []
spent_money = []
profit = 0
final_money = 0

for each_item in collection_of_items:
    index = each_item.split("->")
    item_type = index[0]
    item_price = float(index[1])
    valid_price = False

    if budget < item_price:
        continue

    if item_type == "Clothes":
        if item_price <= 50:
            valid_price = True
    elif item_type == "Shoes":
        if item_price <= 35:
            valid_price = True
    elif item_type == "Accessories":
        if item_price <= 20.50:
            valid_price = True

    if valid_price:
        budget -= item_price
        spent_money.append(item_price)
        each_item_new_price = (item_price * 0.4) + item_price
        list_new_prices.append(each_item_new_price)

profit = sum(list_new_prices) - sum(spent_money)
final_money = budget + sum(list_new_prices)


for item in list_new_prices:
    print(f'{item:.2f}', end=' ')

print()
print(f"Profit: {profit :.2f}")
if final_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
