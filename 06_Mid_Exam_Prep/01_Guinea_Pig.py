food_in_kg = float(input())
hay_in_kg = float(input())
cover_in_kg = float(input())
pigs_weight_in_kg = float(input())

# need to convert everything in gr
food_in_gr = food_in_kg * 1000
hay_in_gr = hay_in_kg * 1000
cover_in_gr = cover_in_kg * 1000
pigs_weight_in_gr = pigs_weight_in_kg * 1000

food_is_enough = True
for days in range(1, 30 + 1):
    food_in_gr -= 300  # every day eats 300gr
    if days % 2 == 0:  # every second day
        hay_in_gr -= food_in_gr * 0.05

    if days % 3 == 0:
        cover_in_gr -= pigs_weight_in_gr * 1/3

    if food_in_gr < 0 or hay_in_gr < 0 or cover_in_gr < 0:
        food_is_enough = False
        break
if food_is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_gr / 1000 :.2f}, "
          f"Hay: {hay_in_gr / 1000 :.2f}, Cover: {cover_in_gr / 1000 :.2f}.")
else:
    print("Merry must go to the pet store!")