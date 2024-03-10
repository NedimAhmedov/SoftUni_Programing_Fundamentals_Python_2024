product_quantities = input().split()
products_to_search = input().split()
bakery = {}

for i in range(0, len(product_quantities), 2):
    key = product_quantities[i]
    value = product_quantities[i + 1]
    bakery[key] = int(value)  # key : value

for each_product in products_to_search:
    if each_product in bakery.keys():
        print(f"We have {bakery[each_product]} of {each_product} left")
    else:
        print(f"Sorry, we don't have {each_product}")