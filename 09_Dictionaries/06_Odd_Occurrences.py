words = input().split()
dictionary = {}

for each_word in words:
    word_lower = each_word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0  # ако word_lower не е в dictionary, го добавяме като key: each_word и value: 0
    dictionary[word_lower] += 1  # увеличаваме value с 1, ако word_lower е в dictionary му вдигаме value с 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
