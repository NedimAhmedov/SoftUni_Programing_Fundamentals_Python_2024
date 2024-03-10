initial_health = 100
initial_bitcoin = 0
managed_rooms = 0

been_killed = False

dungeons_rooms = input().split("|")
for each_room in dungeons_rooms:
    managed_rooms += 1
    each_room = each_room.split()
    number = int(each_room[1])
    action = each_room[0]

    if action == "potion":
        temp_health = initial_health
        initial_health += number
        if initial_health > 100:
            initial_health = 100
        amount = initial_health - temp_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {initial_health} hp.")

    elif action == "chest":
        initial_bitcoin += number
        print(f"You found {number} bitcoins.")

    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {action}.")
        else:
            been_killed = True
            break

if been_killed:
    print(f"You died! Killed by {action}.")
    print(f"Best room: {managed_rooms}")

else:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")