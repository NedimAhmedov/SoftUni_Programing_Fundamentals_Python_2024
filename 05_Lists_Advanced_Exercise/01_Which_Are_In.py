first_sequence = input().split(", ")
second_sequence = input().split(", ")

filtered_sequence = []

for each_word1 in first_sequence:
    for each_word2 in second_sequence:
        if each_word1 in each_word2:
            filtered_sequence.append(each_word1)
            break  # brake - защото, ако думата се среща 2 пъти, ще се дублира накрая
print(filtered_sequence)