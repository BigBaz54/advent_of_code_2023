from path_between_galaxies import parse_input, shortest_path
import time


if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        input_str = f.read()
    start = time.perf_counter()
    pi = parse_input(input_str)
    galaxies = pi[0]
    empty_rows = pi[1]
    empty_cols = pi[2]
    s = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            s += shortest_path(*galaxies[i], *galaxies[j], empty_rows, empty_cols)
    print(time.perf_counter() - start)
    print(s)