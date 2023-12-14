from total_load import parse_input, total_load


if __name__ == '__main__':
    with open('my_input.txt') as f:
        instr = f.read()
    map_lines = parse_input(instr)
    print(total_load(map_lines))