def parse_input(input_str):
    """
    Parses the input string into a list of galaxies after expanding the universe
    """
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    galaxies = []
    current_line = 0
    while current_line < len(lines):
        if '#' not in lines[current_line]:
            lines.insert(current_line, lines[current_line][:])
            current_line += 1
        current_line += 1
    
    current_col = 0
    while current_col < len(lines[0]):
        has_galaxy = False
        for i, c in enumerate([line[current_col] for line in lines]):
            if c == '#':
                galaxies.append((i, current_col))
                has_galaxy = True
        if not has_galaxy:
            for i in range(len(lines)):
                lines[i] = lines[i][:current_col] + '.' + lines[i][current_col:]
            current_col += 1
        current_col += 1
    return galaxies

def shortest_path(i1, j1, i2, j2):
    """
    Returns the shortest path between two galaxies
    """
    return abs(i1 - i2) + abs(j1 - j2)


if __name__ == '__main__':
    galaxies = parse_input('...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....')
    # print(galaxies)
    print(shortest_path(*galaxies[2], *galaxies[4]))
    print(shortest_path(*galaxies[0], *galaxies[-1]))