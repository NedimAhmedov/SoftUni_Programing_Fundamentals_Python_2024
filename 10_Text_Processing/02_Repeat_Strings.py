word_string = input().split()
repeated_string = ""
for each_word in word_string:
    repeated_string += each_word * len(each_word)
print(repeated_string)