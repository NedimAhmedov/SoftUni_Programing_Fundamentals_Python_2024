initial_treasure_chest = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    split_command = command.split()
    action = split_command[0]

    if action == "Loot":
        for item in range(1, len(split_command)):
            if split_command[item] not in initial_treasure_chest:
                initial_treasure_chest.insert(0, split_command[item])

    elif action == "Drop":
        index = int(split_command[-1])
        if index < len(initial_treasure_chest):
            removed = initial_treasure_chest.pop(index)
            initial_treasure_chest.append(removed)

    elif action == "Steal":
        count_steals = min(int(split_command[-1]), len(initial_treasure_chest)) #if the items are not enough to fulfill the command, take as much as there are
        stolen_items = []
        for steal in range(count_steals, 0, -1):
            stolen_items.append(initial_treasure_chest[-steal])
            initial_treasure_chest.remove(initial_treasure_chest[-steal])
        print(*stolen_items, sep=', ')          #print the stolen items

items_length_sum = 0
if len(initial_treasure_chest) > 0:
    for item in initial_treasure_chest:
        items_length_sum += len(item)
    average_treasure_gain = items_length_sum / len(initial_treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")