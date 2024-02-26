number = int(input())

for cycle_one in range(number):
    first = chr(cycle_one + 97)  # +97 защото от там почват символите от а до ц
    for cycle_two in  range(number):
        second = chr(cycle_two + 97)
        for cycle_three in range(number):
            third = chr(cycle_three + 97)
            print(f"{first}{second}{third}")