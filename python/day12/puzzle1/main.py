from damage_arrangements import parse_input, damage_arrangements


if __name__ == '__main__':
    with open('my_input.txt') as f:
        instr = f.read()
    rows = parse_input(instr)
    s = 0
    for row in rows:
        s += damage_arrangements(row)
    print(s)
