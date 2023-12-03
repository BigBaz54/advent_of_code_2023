import time
from part_numbers import *

if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        lines = f.readlines()
    # Method 1 : twice as fast but unreadable
    start = time.perf_counter()
    s = 0
    for i in range(0, len(lines)):
        one_line = lines[i].strip()
        next_line = lines[i+1].strip() if i < len(lines) - 1 else '.'*140
        previous_line = lines[i-1].strip() if i > 0 else '.'*140
        s += sum(part_numbers(one_line, previous_line, next_line))
    end = time.perf_counter()
    print(end - start)
    print(s)
    print()

    # Method 2 : a bit slower but clearer imo
    # (and useful for part 2 (maybe (please?)))
    start = time.perf_counter()
    parsed_lines = parse_input(lines)
    s = 0
    for i in range(0, len(parsed_lines)):
        one_line = parsed_lines[i]
        next_line = parsed_lines[i+1] if i < len(parsed_lines) - 1 else ([], [])
        previous_line = parsed_lines[i-1] if i > 0 else ([], [])
        s += sum(part_numbers2(one_line, previous_line, next_line))
    end = time.perf_counter()
    print(end - start)
    print(s)

