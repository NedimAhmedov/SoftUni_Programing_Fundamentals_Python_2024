sequence_of_integers = list(map(int, input().split()))

average_number = sum(sequence_of_integers) / len(sequence_of_integers)

filtered_sequences = [x for x in sorted(sequence_of_integers, reverse=True) if x > average_number]

if len(filtered_sequences) != 0:
    print(" ".join(map(str, filtered_sequences[:5])))

else:
    print("No")