money_as_string = input().split(", ")  # парите като стринг
#money_as_integer = [int(money) for money in input().split(", ")]  # съкратен вариант за превръщане от стринг в инт
count_of_beggars = int(input())
money_as_integer = []
for money in money_as_string:
    money_as_integer.append(int(money))  # парите като инт в нов лист

final_sum = []
start_index = 0

for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integer), count_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
print(final_sum)