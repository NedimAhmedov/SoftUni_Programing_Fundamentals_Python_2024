text = input()
symbols_count = []
last_string = ""
final_string = ""
repetition = ""
for index in range(len(text)):
    if not text[index].isdigit():
        last_string += text[index]
        symbols_count.append(text[index].lower())
    else:
        # we have digit
        for next_symbol in range(index, len(text)):  # въртим цикъл от индекса до края, за да проверим дали числото е повече от 1 цифра
            if not text[next_symbol].isdigit():
                break
            repetition += text[next_symbol]
        final_string += last_string.upper() * int(repetition)
        last_string = ""
        repetition = ""
print(f"Unique symbols used: {len(set(symbols_count))}")
print(final_string)
