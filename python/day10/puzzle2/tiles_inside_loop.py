def parse_input(input_str):
    lines = input_str.splitlines()
    pipes_map = [line.strip() for line in lines]
    return pipes_map

def tiles_of_loop(pipes_map):
    i, j = starting_point(pipes_map)
    paths_starts = paths(pipes_map, i, j)
    first_path_prev = [i, j]
    second_path_prev = [i, j]
    first_path = [*paths_starts[0]]
    second_path = [*paths_starts[1]]
    loop_tiles = [(i, j), paths_starts[0], paths_starts[1]]
    while first_path != second_path:
        for path, path_prev in zip([first_path, second_path], [first_path_prev, second_path_prev]):
            i, j = path[0], path[1]
            i_prev, j_prev = path_prev[0], path_prev[1]
            path_prev[0] = i
            path_prev[1] = j
            pipe = pipes_map[i][j]
            if pipe == '|':
                if i_prev == i + 1:
                    path[0] = i - 1
                    path[1] = j
                else:
                    path[0] = i + 1
                    path[1] = j
                loop_tiles.append((path[0], path[1]))
                continue
            if pipe == '-':
                if j_prev == j + 1:
                    path[1] = j - 1
                    path[0] = i
                else:
                    path[1] = j + 1
                    path[0] = i
                loop_tiles.append((path[0], path[1]))
                continue
            if pipe == 'L':
                if i_prev == i - 1:
                    path[1] = j + 1
                    path[0] = i
                else:
                    path[0] = i - 1
                    path[1] = j
                loop_tiles.append((path[0], path[1]))
                continue
            if pipe == 'J':
                if i_prev == i - 1:
                    path[1] = j - 1
                    path[0] = i
                else:
                    path[0] = i - 1
                    path[1] = j
                loop_tiles.append((path[0], path[1]))
                continue
            if pipe == '7':
                if i_prev == i + 1:
                    path[1] = j - 1
                    path[0] = i
                else:
                    path[0] = i + 1
                    path[1] = j
                loop_tiles.append((path[0], path[1]))
                continue
            if pipe == 'F':
                if i_prev == i + 1:
                    path[1] = j + 1
                    path[0] = i
                else:
                    path[0] = i + 1
                    path[1] = j
                loop_tiles.append((path[0], path[1]))
    loop_tiles.pop()
    return loop_tiles

def starting_point(pipes_map):
    for i, line in enumerate(pipes_map):
        for j, tile in enumerate(line):
            if tile == 'S':
                return i, j
            
def paths(pipes_map, i, j):
    paths = [-1, -1]
    path = 0
    if (i > 0) and (pipes_map[i-1][j] in '|F7'):
        paths[path] = (i-1, j)
        path += 1
    if (i < len(pipes_map) - 1) and (pipes_map[i+1][j] in '|LJ'):
        paths[path] = (i+1, j)
        path += 1
    if (j > 0) and (pipes_map[i][j-1] in '-LF'):
        paths[path] = (i, j-1)
        path += 1
    if (j < len(pipes_map[0]) - 1) and (pipes_map[i][j+1] in '-7J'):
        paths[path] = (i, j+1)
        path += 1
    return paths

def tiles_inside_loop(pipes_map):
    loop_tiles = tiles_of_loop(pipes_map)
    tiles_inside = 0
    for i, line in enumerate(pipes_map):
        inside = 0 # inside = 1 if the tiles after this one are inside, 0 otherwise
        for j, t in enumerate(line):
            # if i == 4:
            #     print(tiles_inside)
            #     print(inside)
            if (i,j) in loop_tiles:
                if t == 'S':
                    # replace S with the right tile
                    if (i > 0) and ((i-1,j) in loop_tiles) and (pipes_map[i-1][j] in 'F7|'):
                        if (j > 0) and ((i,j-1) in loop_tiles) and (pipes_map[i][j-1] in '-LF'):
                            t = 'J'
                        elif (j < len(line) - 1) and ((i,j+1) in loop_tiles) and (pipes_map[i][j+1] in '-J7'):
                            t = 'L'
                        elif (pipes_map[i+1][j] in '|LJ'):
                            t = '|'
                    elif (i < len(pipes_map) - 1) and ((i+1,j) in loop_tiles) and (pipes_map[i+1][j] in '|JL'):
                        if (j > 0) and ((i,j-1) in loop_tiles) and (pipes_map[i][j-1] in '-LF'):
                            t = '7'
                        elif (pipes_map[i][j+1] in '-J7'):
                            t = 'F'
                    else:
                        t = '-'
                if t == '|':
                    inside = 1 - inside
                elif t == '-':
                    continue
                elif t in 'LF':
                    temp = t
                elif t == 'J' and temp == 'L':
                    continue
                elif t == 'J' and temp == 'F':
                    inside = 1 - inside
                elif t == '7' and temp == 'F':
                    continue
                elif t == '7' and temp == 'L':
                    inside = 1 - inside
            else: 
                tiles_inside += inside
    return tiles_inside
          

if __name__ == '__main__':
    # pi = parse_input('..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...')
    # pi = parse_input('..........\n.S------7.\n.|F----7|.\n.||....||.\n.||....||.\n.|L-7F-J|.\n.|..||..|.\n.L--JL--J.\n..........')
    # pi = parse_input('FF7FSF7F7F7F7F7F---7\nL|LJ||||||||||||F--J\nFL-7LJLJ||||||LJL-77\nF--JF--7||LJLJIF7FJ-\nL---JF-JLJIIIIFJLJJ7\n|F|F-JF---7IIIL7L|7|\n|FFJF7L7F-JF7IIL---7\n7-L-JL7||F7|L7F-7F7|\nL.L7LFJ|||||FJL7||LJ\nL7JLJL-JLJLJL--JLJ.L')
    pi = parse_input('.F----7F7F7F7F-7....\n.|F--7||||||||FJ....\n.||.FJ||||||||L7....\nFJL7L7LJLJ||LJ.L-7..\nL--J.L7...LJS7F-7L7.\n....F-J..F7FJ|L7L7L7\n....L7.F7||L7|.L7L7|\n.....|FJLJ|FJ|F7|.LJ\n....FJL-7.||.||||...\n....L---J.LJ.LJLJ...')
    # print(starting_point(pi))
    # print(paths(pi, *starting_point(pi)))
    print(tiles_inside_loop(pi))