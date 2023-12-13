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

def have_exactly_one_difference(line1, line2):
    difference = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            difference += 1
        if difference > 1:
            return False
    return difference == 1

def reflection_line(map_lines):
    x_len = len(map_lines[0])
    y_len = len(map_lines)

    # Looking for vertical lines that are 1 smudge away to be a line of reflection
    # Line of reflection i is on the right of the line i
    potential_vertical_lines = [(j, 0) for j in range(x_len - 1)]
    for line in map_lines:
        if potential_vertical_lines == []:
            break

        new_potential_vertical_lines = []
        for j, count in potential_vertical_lines:
            left_part = line[:j+1]
            left_part = left_part[::-1]
            right_part = line[j+1:]
            min_len = min(len(left_part), len(right_part))
            if have_exactly_one_difference(left_part[:min_len], right_part[:min_len]) and count == 0:
                new_potential_vertical_lines.append((j, 1))
            if left_part[:min_len] == right_part[:min_len]:
                new_potential_vertical_lines.append((j, count))

        potential_vertical_lines = new_potential_vertical_lines.copy()
    
    smudged_vertical_lines = [line for line in potential_vertical_lines if line[1] == 1]
    if smudged_vertical_lines != []:
        # Returning the number of lines at the left of the line of reflection
        return smudged_vertical_lines[0][0] + 1
    
    # Looking for horizontal lines that are 1 smudge away to be a line of reflection
    # Line of reflection i is on the bottom of the line i
    potential_horizontal_lines = [(i, 0) for i in range(y_len - 1)]
    for j in range(x_len):
        column = [line[j] for line in map_lines]
        if potential_horizontal_lines == []:
            break

        new_potential_horizontal_lines = []
        for i, count in potential_horizontal_lines:
            top_part = column[:i+1]
            top_part = top_part[::-1]
            bottom_part = column[i+1:]
            min_len = min(len(top_part), len(bottom_part))
            if have_exactly_one_difference(top_part[:min_len], bottom_part[:min_len]) and count == 0:
                new_potential_horizontal_lines.append((i, 1))
            if top_part[:min_len] == bottom_part[:min_len]:
                new_potential_horizontal_lines.append((i, count))

        potential_horizontal_lines = new_potential_horizontal_lines.copy()

    smudged_horizontal_lines = [line for line in potential_horizontal_lines if line[1] == 1]
    if smudged_horizontal_lines != []:
        # Returning the number of lines above the line of reflection * 100
        return (smudged_horizontal_lines[0][0] + 1) * 100
    

if __name__ == "__main__":
    maps = parse_input("#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#")
    print(maps)
    for map_lines in maps:
        print(reflection_line(map_lines))
