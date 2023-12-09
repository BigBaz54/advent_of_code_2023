def parse_input(input_str):
    lines = input_str.splitlines()
    sequences = [line.split() for line in lines]
    return [[int(x) for x in sequence] for sequence in sequences]

def predict_prev(sequence):
    first_values = [sequence[0]]
    current_seq = sequence
    while sum([x**2 for x in current_seq]) != 0:
        next_seq = []
        for i in range(len(current_seq) - 1):
            next_seq.append(current_seq[i + 1] - current_seq[i])
        current_seq = next_seq[:]
        first_values.append(current_seq[0])
    prev = first_values[-1]
    for i in range(len(first_values) - 2, -1, -1):
        prev = first_values[i] - prev
    return prev


if __name__ == '__main__':
    pi = parse_input('0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45')
    for seq in pi:
        print(predict_prev(seq))