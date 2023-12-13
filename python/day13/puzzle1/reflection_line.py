def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    maps = []
    current_map = []
    for line in lines:
        if line == "":
            maps.append(current_map)
            current_map = []
        else:
            current_map.append(line)
    maps.append(current_map)
    return maps

def reflection_line(map_lines):
    x_len = len(map_lines[0])
    y_len = len(map_lines)

    # Looking for vertical line of reflection
    # Line of reflection i is on the right of the line i
    potential_vertical_lines = list(range(x_len - 1))
    for line in map_lines:
        if potential_vertical_lines == []:
            break

        new_potential_vertical_lines = []
        for j in potential_vertical_lines:
            left_part = line[:j+1]
            left_part = left_part[::-1]
            right_part = line[j+1:]
            min_len = min(len(left_part), len(right_part))
            if left_part[:min_len] == right_part[:min_len]:
                new_potential_vertical_lines.append(j)

        potential_vertical_lines = new_potential_vertical_lines.copy()
    
    if potential_vertical_lines != []:
        # Returning the number of lines at the left of the line of reflection
        return potential_vertical_lines[0] + 1
    
    # Looking for horizontal line of reflection
    # Line of reflection i is on the bottom of the line i
    potential_horizontal_lines = list(range(y_len - 1))
    for j in range(x_len):
        column = [line[j] for line in map_lines]
        if potential_horizontal_lines == []:
            break

        new_potential_horizontal_lines = []
        for i in potential_horizontal_lines:
            top_part = column[:i+1]
            top_part = top_part[::-1]
            bottom_part = column[i+1:]
            min_len = min(len(top_part), len(bottom_part))
            if top_part[:min_len] == bottom_part[:min_len]:
                new_potential_horizontal_lines.append(i)

        potential_horizontal_lines = new_potential_horizontal_lines.copy()

    if potential_horizontal_lines != []:
        # Returning the number of lines above the line of reflection * 100
        return (potential_horizontal_lines[0] + 1) * 100
    

if __name__ == "__main__":
    maps = parse_input("#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#")
    print(maps)
    for map_lines in maps:
        print(reflection_line(map_lines))
