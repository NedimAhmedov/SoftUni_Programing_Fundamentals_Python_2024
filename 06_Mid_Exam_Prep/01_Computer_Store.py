total_price_without_taxes = 0

command = input()
while command != "special" or command != "regular":

    if command == "special" or command == "regular":
        break

    part_price = command
    if float(part_price) < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += float(part_price)

    command = input()

taxes = total_price_without_taxes * 0.2
total_price = total_price_without_taxes + taxes

if command == "special":
    total_price = total_price * 0.9

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes :.2f}$")
    print(f"Taxes: {taxes :.2f}$")
    print("-----------")
    print(f"Total price: {total_price :.2f}$")
