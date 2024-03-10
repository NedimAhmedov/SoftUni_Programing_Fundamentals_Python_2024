sequence_of_elements = input().split()
moves_counter = 0

while True:
    command = input()
    moves_counter += 1
    if command == "end":
        print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
        break


    indexes = command.split()
    first_index = int(indexes[0])
    second_index = int(indexes[1])

    if first_index > len(sequence_of_elements) - 1 or first_index < 0 or \
            second_index > len(sequence_of_elements) - 1 or second_index < 0:
        mid_index = len(sequence_of_elements) // 2
        sequence_of_elements.insert(mid_index, f'-{moves_counter}a')
        sequence_of_elements.insert(mid_index, f'-{moves_counter}a')
        print("Invalid input! Adding additional elements to the board")

    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        second_element = sequence_of_elements[second_index]
        sequence_of_elements.pop(first_index)
        sequence_of_elements.remove(second_element)

    else:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {moves_counter} turns!")
        exit()



