import re

bought_furniture = []
total_cost = 0
regex = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"  # ? означава може да я има точката може и да я няма (може да се ползва и *)
while True:
    text = input()

    if text == "Purchase":
        break

    match = re.search(regex, text)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost :.2f}")