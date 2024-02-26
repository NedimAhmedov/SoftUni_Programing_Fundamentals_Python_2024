quantity_of_decoration = int(input())
days_left_until_christmas = int(input())

total_cost = 0
points = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for current_day in range(1, days_left_until_christmas + 1):  # подробно проверяваме, защото ни е важно да са подредени дните
    if current_day % 11 == 0:  #  проверяваме го най-горе, защото променяме основната мерна единица, която променя разходите
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decoration * ornament_set
        points += 5
    if current_day % 3 == 0:  #  отделни иф проверки, защото един ден може да е и трети и пети (15ти ден е такъв)
        total_cost += quantity_of_decoration * (tree_skirt + tree_garland)
        points += 10 + 3
    if current_day % 5 == 0:
        total_cost += quantity_of_decoration * tree_lights
        points += 17
        if current_day % 3 == 0:  #  така проверяваме дали денят е и 3ти
            points += 30
    if current_day % 10 == 0:
        points -= 20
        total_cost += tree_skirt + tree_garland + tree_lights
if days_left_until_christmas % 10 == 0:  # последният ден е 10ти пров
    points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {points}")
