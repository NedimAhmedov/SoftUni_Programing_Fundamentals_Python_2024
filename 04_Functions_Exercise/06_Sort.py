list_of_numbers = input().split()
list_of_numbers_as_int = []
for each_number in list_of_numbers:
    list_of_numbers_as_int.append(int(each_number))
list_of_numbers_as_int = sorted(list_of_numbers_as_int)  #  reverse = True - сортира в обратен ред
print(list_of_numbers_as_int)
