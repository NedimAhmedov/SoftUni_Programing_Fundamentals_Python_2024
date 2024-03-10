journal = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        print(*journal, sep=", ")
        break

    split_command = command.split(" - ")
    action = split_command[0]

    if action == "Collect":
        item = split_command[1]
        if item not in journal:
            journal.append(item)

    if action == "Drop":
        item = split_command[1]
        if item in journal:
            journal.remove(item)

    if action == "Combine Items":
        items = split_command[1]
        splitted_items = items.split(":")
        old_item = splitted_items[0]
        new_item = splitted_items[1]
        if old_item in journal:
            old_item_index = journal.index(old_item)
            journal.insert(old_item_index + 1, new_item)


    if action == "Renew":
        item = split_command[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)
