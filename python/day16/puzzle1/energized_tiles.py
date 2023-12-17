def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    map_lines = [[] for _ in range(len(lines))]
    map_cols = [[] for _ in range(len(lines[0]))]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in '/\\|-':
                map_lines[i].append((c, j, []))
                map_cols[j].append((c, i, []))
    return map_lines, map_cols, (len(lines), len(lines[0]))

def cast_beam_rec(from_i, from_j, direction, map_lines, map_cols, energized_tiles, size):
    # print(from_i, from_j, direction)
    n = size[0]
    m = size[1]

    # Fills the energized_tiles matrix with True for all tiles that will be energized by the beam.
    if direction == 'up':
        # We iterate over the mirror and splitter tiles above the current tile from bottom to top.
        for c, i, used_from in map_cols[from_j][::-1]:
            if i <= from_i:
                # We can energize the tiles crossed by the beam and the tile the beam is cast from and the tile the beam will reflect on.
                for k in range(from_i, i - 1, -1):
                    energized_tiles[k][from_j] = True
                
                # We keep track of the directions from which the tile has already been energized
                # to avoid infinite loops.
                if is_tile_used(c, used_from, direction):
                    return
                else:
                    used_from.append(direction)

                # If the tile has not been energized from the current direction, we reflect the beam.
                if c == '|':
                    if i - 1 >= 0:
                        cast_beam_rec(i - 1, from_j, 'up', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '/':
                    if from_j + 1 < m:
                        cast_beam_rec(i, from_j + 1, 'right', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '\\':
                    if from_j - 1 >= 0:
                        cast_beam_rec(i, from_j - 1, 'left', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '-':
                    if from_j - 1 >= 0:
                        cast_beam_rec(i, from_j - 1, 'left', map_lines, map_cols, energized_tiles, size)
                    if from_j + 1 < m:
                        cast_beam_rec(i, from_j + 1, 'right', map_lines, map_cols, energized_tiles, size)
                    break
        else:
            # If we didn't find a mirror or splitter tile above the current tile, we energize all tiles above and the current tile.
            for k in range(from_i, -1, -1):
                energized_tiles[k][from_j] = True
    
    elif direction == 'down':
        # We iterate over the mirror and splitter tiles below the current tile from top to bottom.
        for c, i, used_from in map_cols[from_j]:
            if i >= from_i:
                # We can energize the tiles crossed by the beam and the tile the beam is cast from and the tile the beam will reflect on.
                for k in range(from_i, i + 1):
                    energized_tiles[k][from_j] = True
                
                # We keep track of the directions from which the tile has already been energized
                # to avoid infinite loops.
                if is_tile_used(c, used_from, direction):
                    return
                else:
                    used_from.append(direction)

                # If the tile has not been energized from the current direction, we reflect the beam.
                if c == '|':
                    if i + 1 < n:
                        cast_beam_rec(i + 1, from_j, 'down', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '/':
                    if from_j - 1 >= 0:
                        cast_beam_rec(i, from_j - 1, 'left', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '\\':
                    if from_j + 1 < m:
                        cast_beam_rec(i, from_j + 1, 'right', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '-':
                    if from_j - 1 >= 0:
                        cast_beam_rec(i, from_j - 1, 'left', map_lines, map_cols, energized_tiles, size)
                    if from_j + 1 < m:
                        cast_beam_rec(i, from_j + 1, 'right', map_lines, map_cols, energized_tiles, size)
                    break
        else:
            # If we didn't find a mirror or splitter tile below the current tile, we energize all tiles below and the current tile.
            for k in range(from_i, n):
                energized_tiles[k][from_j] = True

    elif direction == 'left':
        # We iterate over the mirror and splitter tiles to the left of the current tile from right to left.
        for c, j, used_from in map_lines[from_i][::-1]:
            if j <= from_j:
                # We can energize the tiles crossed by the beam and the tile the beam is cast from and the tile the beam will reflect on.
                for k in range(from_j, j - 1, -1):
                    energized_tiles[from_i][k] = True
                
                # We keep track of the directions from which the tile has already been energized
                # to avoid infinite loops.
                if is_tile_used(c, used_from, direction):
                    return
                else:
                    used_from.append(direction)

                # If the tile has not been energized from the current direction, we reflect the beam.
                if c == '-':
                    if j - 1 >= 0:
                        cast_beam_rec(from_i, j - 1, 'left', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '/':
                    if from_i + 1 < n:
                        cast_beam_rec(from_i + 1, j, 'down', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '\\':
                    if from_i - 1 >= 0:
                        cast_beam_rec(from_i - 1, j, 'up', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '|':
                    if from_i - 1 >= 0:
                        cast_beam_rec(from_i - 1, j, 'up', map_lines, map_cols, energized_tiles, size)
                    if from_i + 1 < n:
                        cast_beam_rec(from_i + 1, j, 'down', map_lines, map_cols, energized_tiles, size)
                    break
        else:
            # If we didn't find a mirror or splitter tile to the left of the current tile, we energize all tiles to the left and the current tile.
            for k in range(from_j, -1, -1):
                energized_tiles[from_i][k] = True

    elif direction == 'right':
        # We iterate over the mirror and splitter tiles to the right of the current tile from left to right.
        for c, j, used_from in map_lines[from_i]:
            if j >= from_j:
                # We can energize the tiles crossed by the beam and the tile the beam is cast from and the tile the beam will reflect on.
                for k in range(from_j, j + 1):
                    energized_tiles[from_i][k] = True
                
                # We keep track of the directions from which the tile has already been energized
                # to avoid infinite loops.
                if is_tile_used(c, used_from, direction):
                    return
                else:
                    used_from.append(direction)

                # If the tile has not been energized from the current direction, we reflect the beam.
                if c == '-':
                    if j + 1 < m:
                        cast_beam_rec(from_i, j + 1, 'right', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '/':
                    if from_i - 1 >= 0:
                        cast_beam_rec(from_i - 1, j, 'up', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '\\':
                    if from_i + 1 < n:
                        cast_beam_rec(from_i + 1, j, 'down', map_lines, map_cols, energized_tiles, size)
                    break
                elif c == '|':
                    if from_i - 1 >= 0:
                        cast_beam_rec(from_i - 1, j, 'up', map_lines, map_cols, energized_tiles, size)
                    if from_i + 1 < n:
                        cast_beam_rec(from_i + 1, j, 'down', map_lines, map_cols, energized_tiles, size)
                    break
        else:
            # If we didn't find a mirror or splitter tile to the right of the current tile, we energize all tiles to the right and the current tile.
            for k in range(from_j, m):
                energized_tiles[from_i][k] = True

def cast_beam(map_lines, map_cols, size):
    n = size[0]
    m = size[1]
    # We initialize the energized_tiles matrix with False for all tiles.
    energized_tiles = [[False for _ in range(m)] for _ in range(n)]
    # We cast the first beam from the top-left corner towards the right.
    cast_beam_rec(0, 0, 'right', map_lines, map_cols, energized_tiles, size)
    return energized_tiles

def is_tile_used(c, used_from, direction):
    if used_from == []:
        return False
    
    if c == '|':
        if direction == 'up' or direction == 'down':
            return 'up' in used_from or 'down' in used_from
        else:
            return 'left' in used_from or 'right' in used_from
    elif c == '-':
        if direction == 'left' or direction == 'right':
            return 'left' in used_from or 'right' in used_from
        else:
            return 'up' in used_from or 'down' in used_from
    elif c == '/':
        if direction == 'up' or direction == 'left':
            return 'up' in used_from or 'left' in used_from
        else:
            return 'down' in used_from or 'right' in used_from
    elif c == '\\':
        if direction == 'up' or direction == 'right':
            return 'up' in used_from or 'right' in used_from
        else:
            return 'down' in used_from or 'left' in used_from

def count_energized_tiles(energized_tiles):
    count = 0
    for i in range(len(energized_tiles)):
        for j in range(len(energized_tiles[0])):
            if energized_tiles[i][j]:
                count += 1
    return count


if __name__ == '__main__':
    map_lines, map_cols, size = parse_input('.|...\....\n|.-.\\.....\n.....|-...\n........|.\n..........\n.........\\\n..../.\\\\..\n.-.-/..|..\n.|....-|.\\\n..//.|....')
    energized_tiles = cast_beam(map_lines, map_cols, size)
    print(count_energized_tiles(energized_tiles))
    for line in energized_tiles:
        for c in line:
            print('#' if c else '.', end='')
        print('', end='\n')

