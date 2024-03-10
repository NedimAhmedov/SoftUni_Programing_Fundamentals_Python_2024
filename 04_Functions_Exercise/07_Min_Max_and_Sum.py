list_of_numbers = input().split()
list_of_numbers_as_int = []
for each_number in list_of_numbers:
    list_of_numbers_as_int.append(int(each_number))

print(f"The minimum number is {min(list_of_numbers_as_int)}")
print(f"The maximum number is {max(list_of_numbers_as_int)}")
print(f"The sum number is: {sum(list_of_numbers_as_int)}")
