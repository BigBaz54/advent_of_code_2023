from hash import parse_input, hash


if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        input_str = f.read()
    steps = parse_input(input_str)
    s = 0
    for step in steps:
        s += hash(step)
    print(s)