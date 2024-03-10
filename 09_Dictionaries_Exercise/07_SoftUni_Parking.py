parking_dict = {}
cars_numb = int(input())
for each_car in range(cars_numb):
    command = input().split()
    action = command[0]
    name = command[1]

    if action == "register":
        reg_number = command[2]
        if name not in parking_dict:
            parking_dict[name] = reg_number
            print(f"{name} registered {reg_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_dict[name]}")

    elif action == "unregister":
        if name not in parking_dict:
            print(f"ERROR: user {name} not found")
        else:
            del parking_dict[name]
            print(f"{name} unregistered successfully")

for key, value in parking_dict.items():
    print(f"{key} => {value}")

