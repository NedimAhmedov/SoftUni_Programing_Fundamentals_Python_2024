fire_cells = input().split("#")
water = int(input())

total_fire = 0
effort = 0
put_out_cells = []

for fire in fire_cells:
    index = fire.split(" = ")
    fire_type = index[0]
    level = int(index[1])
    valid = False

    if water < level:
        continue

    if fire_type == "High":
        if 81 <= level <= 125:
            valid = True
    elif fire_type == "Medium":
        if 51 <= level <= 80:
            valid = True
    elif fire_type == "Low":
        if 1 <= level <= 50:
            valid = True

    if valid:
        put_out_cells.append(level)
        water -= level
        effort += level * 0.25
        total_fire += level

print("Cells:")
for cells in put_out_cells:
    print(f" - {cells}")

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

