initial_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    command = command.split()
    type_of_command = command[0]
    product = command[1]

    if type_of_command == "Urgent":
        if product not in initial_list:
            initial_list.insert(0, product)

    if type_of_command == "Unnecessary":
        if product in initial_list:
            initial_list.remove(product)

    if type_of_command == "Correct":
        new_product = command[2]
        if product in initial_list:
            index = initial_list.index(product)
            initial_list[index] = new_product

    if type_of_command == "Rearrange":
        if product in initial_list:
            initial_list.remove(product)
            initial_list.append(product)

print(', '.join(initial_list))