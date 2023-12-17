from energized_tiles import parse_input, cast_beam, count_energized_tiles


if __name__ == "__main__":
    with open("my_input.txt") as f:
        input_str = f.read()
    map_lines, map_cols, size = parse_input(input_str)
    energized_tiles = cast_beam(map_lines, map_cols, size)
    print(count_energized_tiles(energized_tiles))