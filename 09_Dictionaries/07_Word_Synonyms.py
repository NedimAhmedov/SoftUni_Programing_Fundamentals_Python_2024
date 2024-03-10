count_of_word = int(input())
synonyms = {}
for each_word in range(count_of_word):
    current_word = input()
    synonym = input()

    if current_word not in synonyms.keys():
        synonyms[current_word] = []  # създаваме празен списък с key current word
    synonyms[current_word].append(synonym) # вкарваме в списъка на current_word synonym
for words, synonyms_list in synonyms.items():
    print(f"{words} - {', '.join(synonyms_list)}")