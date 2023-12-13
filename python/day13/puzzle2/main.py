from reflection_line import parse_input, reflection_line
import time


if __name__ == "__main__":
    with open("my_input.txt", "r") as f:
        instr = f.read()
    start = time.perf_counter()
    maps = parse_input(instr)
    s = 0
    for map_lines in maps:
        s += reflection_line(map_lines)
    print(time.perf_counter() - start)
    print(s)