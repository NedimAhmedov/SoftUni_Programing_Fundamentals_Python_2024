my_dict = {}
while True:
    command = input()

    if command == "stop":
        for item_resource, item_quantity in my_dict.items():
            print(f"{item_resource} -> {item_quantity}")
        break

    item_resource = command
    item_quantity = int(input())

    if item_resource not in my_dict:
        my_dict[item_resource] = 0
    my_dict[item_resource] += item_quantity
