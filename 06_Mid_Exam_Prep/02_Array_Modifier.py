array_values = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        print(*array_values, sep=", ")
        break

    split_command = command.split()
    given_command = split_command[0]

    if given_command == "swap":
        first_element = int(split_command[1])
        second_element = int(split_command[2])
        array_values[first_element], array_values[second_element] = \
            array_values[second_element], array_values[first_element]

    if given_command == "multiply":
        first_element = int(split_command[1])
        second_element = int(split_command[2])
        array_values[first_element] *= array_values[second_element]

    if given_command == "decrease":
        array_values = [number - 1 for number in array_values]
