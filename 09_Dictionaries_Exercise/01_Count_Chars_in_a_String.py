string = input().split()
characters_count = {}

for each_word in string:
    for each_char in each_word:
        if each_char not in characters_count:
            characters_count[each_char] = 0
        characters_count[each_char] += 1

for key, value in characters_count.items():
    print(f"{key} -> {value}")