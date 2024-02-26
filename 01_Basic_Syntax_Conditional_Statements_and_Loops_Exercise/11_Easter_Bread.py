budget = float(input())
price_for_kg_flour = float(input())

eggs_pack_price = price_for_kg_flour * 0.75
liter_milk_price = price_for_kg_flour * 1.25
dose_milk_price = liter_milk_price / 4

price_per_one_loaves = eggs_pack_price + price_for_kg_flour + dose_milk_price

loaves = 0
colored_eggs = 0
while budget > price_per_one_loaves:
    budget -= price_per_one_loaves
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {budget:.2f}BGN left.")

