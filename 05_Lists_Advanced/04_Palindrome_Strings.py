word_string = input().split()
searched_palindrome = input()
palindromes = []

for each_word in word_string:
    if each_word == each_word[::-1]:
        palindromes.append(each_word)
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")