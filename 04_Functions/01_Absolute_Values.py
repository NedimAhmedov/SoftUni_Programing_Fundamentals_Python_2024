number_list = input().split()

absolute_numbers_list = []

for number in number_list:
    absolute_numbers_list.append(abs(float(number)))

print(absolute_numbers_list)