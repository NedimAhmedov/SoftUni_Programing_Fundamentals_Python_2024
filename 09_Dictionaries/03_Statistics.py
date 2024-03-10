products = {}

while True:
    command = input()

    if command == "statistics":
        break

    split_command = command.split(": ")
    product = split_command[0]
    quantity = int(split_command[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity

print(f"Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")