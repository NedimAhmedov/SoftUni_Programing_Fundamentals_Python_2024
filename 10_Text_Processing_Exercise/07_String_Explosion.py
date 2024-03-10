explosion_strength = 0
last_string = ""
explosion_string = input()
for index in range(len(explosion_string)):
    # We have explosion
    if explosion_strength > 0 and explosion_string[index] != ">":
        explosion_strength -= 1
    # We have explosion mark
    elif explosion_string[index] == ">":
        last_string += explosion_string[index]
        explosion_strength += int(explosion_string[index + 1])
    # We have normal character
    else:
        last_string += explosion_string[index]
print(last_string)