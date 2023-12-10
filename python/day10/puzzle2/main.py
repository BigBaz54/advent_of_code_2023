from tiles_inside_loop import parse_input, tiles_inside_loop
import time


if __name__ == '__main__':
    with open('my_input.txt') as f:
        in_str = f.read()
    start = time.perf_counter()
    pipes_map = parse_input(in_str)
    print(tiles_inside_loop(pipes_map))
    print(time.perf_counter() - start)