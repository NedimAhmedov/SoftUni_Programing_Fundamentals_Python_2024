numbers = input().split()
rounded_list = []

for each_number in numbers:
    rounded_list.append(round(float(each_number)))

print(rounded_list)