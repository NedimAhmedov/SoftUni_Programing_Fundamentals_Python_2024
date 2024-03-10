encrypted_text = input()
decrypted_text = ""
for each_each_word in encrypted_text:
    for each_char in each_each_word:
       decrypted_char = chr(ord(each_char) + 3)
       decrypted_text += decrypted_char
print(decrypted_text)