force_book_dict = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if "|" in command:
        split_command = command.split(" | ")
        user_is_part_of_the_force = False
        force_side = split_command[0]
        force_user = split_command[1]
        for value in force_book_dict.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_book_dict.keys():
                force_book_dict[force_side] = []
            force_book_dict[force_side].append(force_user)

    elif "->" in command:
        new_split_command = command.split(" -> ")
        new_user = new_split_command[0]
        new_force_side = new_split_command[1]
        for value in force_book_dict.values():
            if new_user in value:
                value.remove(new_user)
                break
        if new_force_side not in force_book_dict.keys():
            force_book_dict[new_force_side] = []
        force_book_dict[new_force_side].append(new_user)
        print(f"{new_user} joins the {new_force_side} side!")

for key, value in force_book_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for each_member in value:
            print(f"! {each_member}")
