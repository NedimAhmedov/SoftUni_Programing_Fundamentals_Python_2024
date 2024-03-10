alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total_sum = 0
sequence_of_strings = input().split()
for each_word in sequence_of_strings:
    first_letter = each_word[0]
    second_letter = each_word[-1]
    number = int(each_word[1:len(each_word) - 1])
    # first letter is lower
    if first_letter in alphabet_list:
        total_sum += number * (alphabet_list.index(first_letter) + 1)
    # first letter is upper
    elif first_letter.isupper() and first_letter.lower() in alphabet_list:
        total_sum += number / (alphabet_list.index(first_letter.lower()) + 1)
    # second letter is lower
    if second_letter in alphabet_list:
        total_sum += alphabet_list.index(second_letter.lower()) + 1
    # second letter is upper
    elif second_letter.isupper() and second_letter.lower() in alphabet_list:
        total_sum = total_sum - (alphabet_list.index(second_letter.lower()) + 1)
print(f"{total_sum :.2f}")
