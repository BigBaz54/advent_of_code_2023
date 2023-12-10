def parse_input(input_str):
    lines = input_str.splitlines()
    pipes_map = [line.strip() for line in lines]
    return pipes_map

def farthest_point_in_loop(pipes_map):
    i, j = starting_point(pipes_map)
    paths_starts = paths(pipes_map, i, j)
    first_path_prev = [i, j]
    second_path_prev = [i, j]
    first_path = [*paths_starts[0]]
    second_path = [*paths_starts[1]]
    steps = 1
    while first_path != second_path:
        steps += 1
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
                continue
            if pipe == '-':
                if j_prev == j + 1:
                    path[1] = j - 1
                    path[0] = i
                else:
                    path[1] = j + 1
                    path[0] = i
                continue
            if pipe == 'L':
                if i_prev == i - 1:
                    path[1] = j + 1
                    path[0] = i
                else:
                    path[0] = i - 1
                    path[1] = j
                continue
            if pipe == 'J':
                if i_prev == i - 1:
                    path[1] = j - 1
                    path[0] = i
                else:
                    path[0] = i - 1
                    path[1] = j
                continue
            if pipe == '7':
                if i_prev == i + 1:
                    path[1] = j - 1
                    path[0] = i
                else:
                    path[0] = i + 1
                    path[1] = j
                continue
            if pipe == 'F':
                if i_prev == i + 1:
                    path[1] = j + 1
                    path[0] = i
                else:
                    path[0] = i + 1
                    path[1] = j
    return steps

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
          

if __name__ == '__main__':
    pi = parse_input('..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...')
    # print(starting_point(pi))
    # print(paths(pi, *starting_point(pi)))
    print(farthest_point_in_loop(pi))