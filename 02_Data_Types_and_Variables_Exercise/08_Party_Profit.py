group_size = int(input())
days = int(input())

coins = 0
for each_day in range(1, days + 1):
    if each_day % 10 == 0:  # тук се променя броя на групата за това трябва да е най-горе
        group_size -= 2
    if each_day % 15 == 0:
        group_size += 5
    if each_day % 3 == 0:
        coins -= (3 * group_size)
    if each_day % 5 == 0:
        coins += (20 * group_size)
        if each_day % 3 == 0:
            coins -= (2 * group_size )
    coins += 50
    coins -= (2 * group_size)  # трябва да е най-долу, защото зависи от броя на групата
sum_coins = coins // group_size
print(f"{group_size} companions received {sum_coins} coins each.")
