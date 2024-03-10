numbers_list = input().split()
numbers_as_int = []
for each_number in numbers_list:
    numbers_as_int.append(int(each_number))


def even_numbers(numbers):
    if numbers % 2 == 0:
        return True
    else:
        return False

evens = filter(even_numbers, numbers_as_int)
evens_list = []

for numbers in evens:
    evens_list.append(numbers)
print(evens_list)
