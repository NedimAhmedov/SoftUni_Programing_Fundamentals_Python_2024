phone_book = {}
command = input()
while "-" in command:
    split_command = command.split("-")
    name = split_command[0]
    phone = split_command[1]

    if name not in phone_book:
        phone_book[name] = 0
    phone_book[name] = phone

    command = input()

number = int(command)
for each_number in range(number):
    name_to_search = input()
    if name_to_search in phone_book:
        print(f"{name_to_search} -> {phone_book[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")