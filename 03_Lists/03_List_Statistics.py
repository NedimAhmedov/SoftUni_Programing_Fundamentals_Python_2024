number = int(input())

positive_list = []
negative_list = []

for cycles in range(number):
    new_number = int(input())
    if new_number >= 0:
        positive_list.append(new_number)
    else:
        negative_list.append(new_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
