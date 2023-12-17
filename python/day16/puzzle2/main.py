from energized_tiles import parse_input, cast_beam, count_energized_tiles, print_energized_tiles
import time


if __name__ == "__main__":
    with open("my_input.txt") as f:
        input_str = f.read()
    parse_start = time.perf_counter()
    map_lines, map_cols, size = parse_input(input_str)
    max_ = 0
    start = time.perf_counter()
    print("Parsing time: ", start - parse_start)
    for i in range(110):
        map_lines, map_cols, size = parse_input(input_str)
        et = cast_beam(i, 0, 'right', map_lines, map_cols, size)
        max_ = max(max_, count_energized_tiles(et))
    for i in range(110):
        map_lines, map_cols, size = parse_input(input_str)
        et = cast_beam(0, i, 'down', map_lines, map_cols, size)
        max_ = max(max_, count_energized_tiles(et))
    for i in range(110):
        map_lines, map_cols, size = parse_input(input_str)
        et = cast_beam(109, i, 'up', map_lines, map_cols, size)
        max_ = max(max_, count_energized_tiles(et))
    for i in range(110):
        map_lines, map_cols, size = parse_input(input_str)
        et = cast_beam(i, 109, 'left', map_lines, map_cols, size)
        max_ = max(max_, count_energized_tiles(et))
    print(max_)
    print("Time: ", time.perf_counter() - start)