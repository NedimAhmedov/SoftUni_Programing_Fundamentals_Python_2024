pirate_ship_status = list(map(int, input().split(">")))
warship_ship_status = list(map(int, input().split(">")))
max_health_capacity = int(input())

while True:
    command = input()
    if command == "Retire":
        break

    split_command = command.split()
    action = split_command[0]

    if action == "Fire":
        index = int(split_command[1])
        damage = int(split_command[2])
        if 0 <= index < len(warship_ship_status):  # проверяваме дали индекса е валиден
            warship_ship_status[index] -= damage

            if warship_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()  # стопираме програмата (по условие)

    elif action == "Defend":
        startIndex = int(split_command[1])
        endIndex = int(split_command[2])
        damage = int(split_command[3])
        if 0 <= startIndex < len(pirate_ship_status):  # проверяваме дали индекса е валиден
            if 0 <= endIndex < len(pirate_ship_status):  # проверяваме дали индекса е валиден
                for i in range(startIndex, endIndex + 1):  # променяме в диапазон
                    pirate_ship_status[i] -= damage

                    if pirate_ship_status[i] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        exit()

    elif action == "Repair":
        index = int(split_command[1])
        health = int(split_command[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_capacity:
                pirate_ship_status[index] = max_health_capacity

    elif action == "Status":
        count_to_be_repaired = 0
        for i in pirate_ship_status:
            if i < max_health_capacity * 0.2:
                count_to_be_repaired += 1
        print(f"{count_to_be_repaired} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_ship_status)}")
