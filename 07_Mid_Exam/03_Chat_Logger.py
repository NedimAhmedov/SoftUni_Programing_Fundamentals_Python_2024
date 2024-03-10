chat_messages = []
while True:
    command = input()
    if command == "end":
        print(*chat_messages, sep="\n")
        break

    split_command = command.split()
    action = split_command[0]

    if action == "Chat":
        message = split_command[1]
        chat_messages.append(message)

    if action == "Delete":
        message = split_command[1]
        if message in chat_messages:
            chat_messages.remove(message)

    if action == "Edit":
        message = split_command[1]
        edited_message = split_command[2]
        if message in chat_messages:
            index_old_mess = chat_messages.index(message)
            chat_messages[index_old_mess] = edited_message

    if action == "Pin":
        message = split_command[1]
        if message in chat_messages:
            chat_messages.remove(message)
            chat_messages.append(message)

    if action == "Spam":
        chat_messages.extend(split_command[1:])