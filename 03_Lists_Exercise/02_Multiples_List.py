factor = int(input())
count = int(input())

my_list = []

for number in range(1, count + 1):  # итерациите са до count, започва се от 1, а не от factor
        my_list.append(number * factor)
print(my_list)