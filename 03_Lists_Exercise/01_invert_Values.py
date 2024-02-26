positive_list = input().split()  # прави лист, който съдържа стрингова разделени с интервал
opposite_list = []
for numbers in positive_list:
    negative_number = -int(numbers)
    opposite_list.append(negative_number)
print(opposite_list)
