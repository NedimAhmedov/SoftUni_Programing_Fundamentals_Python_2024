#characters = input().split(", ")
#dictionaries = {}
#for each_character in characters:
#    dictionaries[each_character] = ord(each_character)
#print(dictionaries)

characters = input().split(", ")
char_dict = {char: ord(char) for char in characters}  #  using comprehension
print(char_dict)