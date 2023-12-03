import time
from gear_ratios import *

if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        lines = f.readlines()

    start = time.perf_counter()
    parsed_lines = parse_input(lines)
    s = 0
    for i in range(0, len(parsed_lines)):
        one_line = parsed_lines[i]
        next_line = parsed_lines[i+1] if i < len(parsed_lines) - 1 else ([], [])
        previous_line = parsed_lines[i-1] if i > 0 else ([], [])
        s += sum(gear_ratios(one_line, previous_line, next_line))
    end = time.perf_counter()
    print(end - start)
    print(s)

