def parse_input(input_str):
    lines = input_str.splitlines()
    sequences = [line.split() for line in lines]
    return [[int(x) for x in sequence] for sequence in sequences]

def predict_next(sequence):
    last_values = [sequence[-1]]
    current_seq = sequence
    while sum([x**2 for x in current_seq]) != 0:
        next_seq = []
        for i in range(len(current_seq) - 1):
            next_seq.append(current_seq[i + 1] - current_seq[i])
        current_seq = next_seq[:]
        last_values.append(current_seq[-1])
    return sum(last_values) 


if __name__ == '__main__':
    pi = parse_input('0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45')
    for seq in pi:
        print(predict_next(seq))