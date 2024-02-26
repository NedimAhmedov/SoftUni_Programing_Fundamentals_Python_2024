number_of_orders = int(input())
total_price_all_orders = 0
for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
        continue
    total_price_per_order = price_per_capsule * days * needed_capsules_per_day
    total_price_all_orders += total_price_per_order
    print(f"The price for the coffee is: ${total_price_per_order :.2f}")
print(f"Total: ${total_price_all_orders :.2f}")