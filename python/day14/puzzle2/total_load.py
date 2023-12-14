import numpy as np

def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    map_ = np.zeros((len(lines), len(lines[0])))
    for i, line in enumerate(lines):
        for j, tile in enumerate(line):
            if tile == 'O':
                map_[i, j] = 1
            elif tile == '#':
                map_[i, j] = 2
    return map_


def tilt_north(map_):
    last_stop_i = [-1 for _ in range(map_.shape[1])]
    new_map = np.zeros_like(map_)
    for i, line in enumerate(map_):
        for j, tile in enumerate(line):
            if tile == 1:
                # A rounded rock that will roll until it's stoppped
                new_map[last_stop_i[j] + 1, j] = 1
                last_stop_i[j] += 1
            elif tile == 2:
                # A cube rock that will not roll
                new_map[i, j] = 2
                last_stop_i[j] = i
    return new_map

def tilt_west(map_):
    last_stop_j = [-1 for _ in range(map_.shape[0])]
    new_map = np.zeros_like(map_)
    for j, line in enumerate(map_.T):
        for i, tile in enumerate(line):
            if tile == 1:
                # A rounded rock that will roll until it's stoppped
                new_map[i, last_stop_j[i] + 1] = 1
                last_stop_j[i] += 1
            elif tile == 2:
                # A cube rock that will not roll
                new_map[i, j] = 2
                last_stop_j[i] = j
    return new_map

def tilt_south(map_):
    last_stop_i = [map_.shape[0] for _ in range(map_.shape[1])]
    new_map = np.zeros_like(map_)
    for i, line in enumerate(map_[::-1]):
        for j, tile in enumerate(line):
            if tile == 1:
                # A rounded rock that will roll until it's stoppped
                new_map[last_stop_i[j] - 1, j] = 1
                last_stop_i[j] -= 1
            elif tile == 2:
                # A cube rock that will not roll
                new_map[map_.shape[0] - 1 - i, j] = 2
                last_stop_i[j] = map_.shape[0] - 1 - i
    return new_map

def tilt_east(map_):
    last_stop_j = [map_.shape[1] for _ in range(map_.shape[0])]
    new_map = np.zeros_like(map_)
    for j, line in enumerate(map_.T[::-1]):
        for i, tile in enumerate(line):
            if tile == 1:
                # A rounded rock that will roll until it's stoppped
                new_map[i, last_stop_j[i] - 1] = 1
                last_stop_j[i] -= 1
            elif tile == 2:
                # A cube rock that will not roll
                new_map[i, map_.shape[1] - j - 1] = 2
                last_stop_j[i] = map_.shape[1] - j - 1
    return new_map

def do_one_cycle(map_):
    map_ = tilt_north(map_)
    map_ = tilt_west(map_)
    map_ = tilt_south(map_)
    map_ = tilt_east(map_)
    return map_

def do_n_cycle(map_, n):
    maps = {map_to_str(map_): 0}
    cycles_done = 0
    while cycles_done < n:
        map_ = do_one_cycle(map_)
        cycles_done += 1
        s = map_to_str(map_)
        if s in maps:
            # We found a cycle
            cycle_length = cycles_done - maps[s]
            cycles_left = n - cycles_done
            cycles_done += cycles_left // cycle_length * cycle_length
        else:
            maps[s] = cycles_done
    return map_

def total_load(map_):
    total_load = 0
    for i, line in enumerate(map_[::-1]):
        for tile in line:
            if tile == 1:
                total_load += i + 1
    return total_load

def print_map(map_):
    for line in map_:
        for tile in line:
            if tile == 0:
                print('.', end='')
            elif tile == 1:
                print('O', end='')
            elif tile == 2:
                print('#', end='')
        print()

def map_to_str(map_):
    s = ''
    for line in map_:
        for tile in line:
            if tile == 0:
                s += '.'
            elif tile == 1:
                s += 'O'
            elif tile == 2:
                s += '#'
        s += '\n'
    return s

if __name__ == '__main__':
    map_ = parse_input('O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#....')
    print(total_load(tilt_north(map_)))
    # print(map_)
    # map_1 = tilt_north(map_)
    # print('All 2s at the same place:', np.all((map_1 == map_) | (map_ == 1) | (map_ == 0)))
    # print('Same number of 1s :', np.sum(map_1 == 1) == np.sum(map_ == 1))
    # map_1 = tilt_west(map_)
    # print('All 2s at the same place:', np.all((map_1 == map_) | (map_ == 1) | (map_ == 0)))
    # print('Same number of 1s :', np.sum(map_1 == 1) == np.sum(map_ == 1))
    # map_1 = tilt_south(map_)
    # print('All 2s at the same place:', np.all((map_1 == map_) | (map_ == 1) | (map_ == 0)))
    # print('Same number of 1s :', np.sum(map_1 == 1) == np.sum(map_ == 1))
    # map_1 = tilt_east(map_)
    # print('All 2s at the same place:', np.all((map_1 == map_) | (map_ == 1) | (map_ == 0)))
    # print('Same number of 1s :', np.sum(map_1 == 1) == np.sum(map_ == 1))
    # map_1 = do_one_cycle(map_)
    # print('All 2s at the same place:', np.all((map_1 == map_) | (map_ == 1) | (map_ == 0)))
    # print('Same number of 1s :', np.sum(map_1 == 1) == np.sum(map_ == 1))

    # maps = {map_to_str(map_): 0}
    # for i in range(1, 100):
    #     map_ = do_one_cycle(map_)
    #     s = map_to_str(map_)
    #     if s in maps:
    #         print('Cycle found at', i)
    #         print('Cycle length:', i - maps[s])
    #         break
    #     else:
    #         maps[s] = i

    print(total_load(do_n_cycle(map_, 1000000000)))