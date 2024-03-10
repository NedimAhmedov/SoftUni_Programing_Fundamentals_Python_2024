route = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())

titan_reached = True

for each_command in route:
    each_command_split = each_command.split()
    action = each_command_split[0]

    if action == "Travel":
        distance_to_travel = int(each_command_split[1])
        if starting_fuel >= distance_to_travel:
            starting_fuel -= distance_to_travel
            print(f"The spaceship travelled {distance_to_travel} light-years.")
        else:
            titan_reached = False
            break

    elif action == "Enemy":
        enemy_armour = int(each_command_split[1])
        if starting_ammunition >= enemy_armour:
            starting_ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")

        elif starting_ammunition < enemy_armour:
            if starting_fuel >= (enemy_armour * 2):
                starting_fuel -= (enemy_armour * 2)
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                titan_reached = False
                break

    elif action == "Repair":
        added_ammunition_fuel = int(each_command_split[1])
        starting_fuel += added_ammunition_fuel
        starting_ammunition += (added_ammunition_fuel * 2)
        print(f"Ammunitions added: {(added_ammunition_fuel * 2)}.")
        print(f"Fuel added: {added_ammunition_fuel}.")

    elif action == "Titan":
        break

if titan_reached:
    print("You have reached Titan, all passengers are safe.")
else:
    print("Mission failed.")

