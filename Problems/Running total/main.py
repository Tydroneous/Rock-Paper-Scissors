sequence = input()
total_seq = [int(sequence[0])]
for i in range(1, len(sequence)):
    total_seq.append(int(total_seq[i - 1]) + int(sequence[i]))

print(total_seq)
