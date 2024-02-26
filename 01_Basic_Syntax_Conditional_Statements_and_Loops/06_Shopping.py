budget = int(input())

command = input()
while command != "End":
    product_price = int(command)
    if product_price <= budget:
        budget -= product_price
    else:
        print("You went in overdraft!")
        break
    command = input()
if command == "End":
    print("You bought everything needed.")