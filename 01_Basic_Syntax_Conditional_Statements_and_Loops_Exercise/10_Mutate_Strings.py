first_string = input()
second_string = input()
las_printed = first_string  # уникалност
for cycles in range(len(first_string)):
    left_part = second_string[0:cycles +1]  # от индекс 0 до индекса, на който се намираме
    right_part = first_string[cycles + 1:]  # от индекса, на който се намирам до края
    new_part = left_part + right_part
    if new_part != las_printed:
        print(new_part)
        las_printed = new_part