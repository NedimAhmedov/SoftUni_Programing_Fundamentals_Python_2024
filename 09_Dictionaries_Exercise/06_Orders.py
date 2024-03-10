orders_dict = {}
while True:
    command = input()
    if command == "buy":
        break

    split_command = command.split()
    product_name = split_command[0]
    product_price = float(split_command[1])
    product_quantity = int(split_command[2])

    if product_name not in orders_dict:
        orders_dict[product_name] = {"product_price": product_price, "product_quantity": product_quantity}  # добавяме повече от 1 value
    else:
        orders_dict[product_name]["product_quantity"] += product_quantity
        orders_dict[product_name]['product_price'] = product_price

for key, value in orders_dict.items():
    total_price = value["product_price"] * value["product_quantity"]
    print(f"{key} -> {total_price :.2f}")
