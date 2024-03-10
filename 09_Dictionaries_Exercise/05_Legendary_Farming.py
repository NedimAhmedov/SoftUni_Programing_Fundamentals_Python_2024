my_dict = {"shards": 0, "fragments": 0, "motes": 0}
goal_reached = False

current_items = input().split()
while not goal_reached:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in my_dict.keys():
            my_dict[key] = 0
        my_dict[key] += value
        if my_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            my_dict["shards"] -= 250
            goal_reached = True
        elif my_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            my_dict["fragments"] -= 250

            goal_reached = True
        elif my_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            my_dict["motes"] -= 250
            goal_reached = True
        if goal_reached:
            break
    if goal_reached:
        break
    current_items = input().split()

for key, value in my_dict.items():
    print(f"{key}: {value}")




