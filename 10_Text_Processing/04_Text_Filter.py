banned_words = input().split(", ")
text = input()
for each_word in banned_words:
    if each_word in text:
        text = text.replace(each_word, "*" * len(each_word))
print(text)