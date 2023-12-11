def parse_input(input_str):
    """
    Parses the input string into a list of galaxies and two lists of rows and columns that are empty.
    """
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    galaxies = []
    current_line = 0
    empty_rows = []
    while current_line < len(lines):
        if '#' not in lines[current_line]:
            empty_rows.append(current_line)
        current_line += 1
    
    current_col = 0
    empty_cols = []
    while current_col < len(lines[0]):
        has_galaxy = False
        for i, c in enumerate([line[current_col] for line in lines]):
            if c == '#':
                galaxies.append((i, current_col))
                has_galaxy = True
        if not has_galaxy:
            empty_cols.append(current_col)
        current_col += 1
    return galaxies, empty_rows, empty_cols

def shortest_path(i1, j1, i2, j2, empty_rows, empty_cols):
    """
    Returns the shortest path between two galaxies taking into account the empty rows and columns that count as 1000000 steps instead of 1.
    """
    steps = abs(i1 - i2) + abs(j1 - j2)
    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)
    for row in empty_rows:
        if row >= i2:
            break
        if row > i1:
            steps += 999999
    for col in empty_cols:
        if col >= j2:
            break
        if col > j1:
            steps += 999999
    return steps


if __name__ == '__main__':
    pi = parse_input('...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....')
    galaxies = pi[0]
    empty_rows = pi[1]
    empty_cols = pi[2]
    print(shortest_path(*galaxies[0], *galaxies[1], empty_rows, empty_cols))