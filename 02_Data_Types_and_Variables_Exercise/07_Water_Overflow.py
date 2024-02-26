lines = int(input())
capacity = 255
poured_water = 0
for cycles in range(lines):
    liters_of_water = int(input())
    if liters_of_water > capacity:
        print("Insufficient capacity!")
        continue
    else:
        poured_water += liters_of_water
        capacity -= liters_of_water
print(poured_water)