# word_string = input().split()
#
# for each_word in word_string:
#     if len(each_word) % 2 == 0:
#         print(each_word)
#

words = input().split()

filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))