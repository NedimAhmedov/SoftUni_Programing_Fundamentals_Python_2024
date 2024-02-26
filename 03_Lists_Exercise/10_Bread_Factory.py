events = input().split("|")
energy = 100
coins = 100
bakery_is_open = True

for event in events:
    event_item = event.split("-")
    type_of_event = event_item[0]
    value_of_event = int(event_item[1])

    if type_of_event == "rest":
        current_energy = energy
        energy += value_of_event
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif type_of_event == "order":
        if energy >= 30:
            energy -= 30
            coins += value_of_event
            print(f"You earned {value_of_event} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value_of_event:
            coins -= value_of_event
            print(f"You bought {type_of_event}.")
        else:
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

else:
    print(f"Closed! Cannot afford {type_of_event}.")
