from damage_arrangements import parse_input, damage_arrangements
import time


if __name__ == '__main__':
    with open('my_input.txt') as f:
        instr = f.read()
    start = time.perf_counter()
    rows = parse_input(instr)
    s = 0
    for row in rows:
        s += damage_arrangements(row)
    print(time.perf_counter() - start)
    print(s)
