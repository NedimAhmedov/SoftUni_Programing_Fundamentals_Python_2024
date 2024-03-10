house_list = list(map(int, input().split("@")))
current_index = 0

while True:
    command = input()

    if command == "Love!":
        break

    jump_length = command.split()
    step = int(jump_length[1])

    if current_index + step <= len(house_list) - 1:
        current_index += step

        if house_list[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            house_list[current_index] -= 2
            if house_list[current_index] == 0:
                print(f"Place {current_index} has Valentine's day." )

    else:
        current_index = 0
        if house_list[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            house_list[current_index] -= 2
            if house_list[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {current_index}.")

if sum(house_list) == 0:
    print(f"Mission was successful.")

else:
    failed_houses = [each_house for each_house in house_list if each_house != 0]
    print(f"Cupid has failed {len(failed_houses)} places.")



