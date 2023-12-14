def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    return lines

def total_load(map_lines):
    last_stop_i = [-1 for _ in range(len(map_lines[0]))]
    total_load = 0
    for i, line in enumerate(map_lines):
        for j, char in enumerate(line):
            if char == 'O':
                # A rounded rock that will roll until it's stoppped
                i_after_roll = last_stop_i[j] + 1
                total_load += len(map_lines) - i_after_roll
                last_stop_i[j] = i_after_roll
            elif char == '#':
                # A cube rock that will not roll
                last_stop_i[j] = i
    return total_load

if __name__ == '__main__':
    map_lines = parse_input('O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#....')
    print(total_load(map_lines))