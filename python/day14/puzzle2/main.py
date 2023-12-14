from total_load import parse_input, total_load, do_n_cycle
import time


if __name__ == '__main__':
    with open('my_input.txt') as f:
        instr = f.read()
    start = time.perf_counter()
    map_ = parse_input(instr)
    print(total_load(do_n_cycle(map_, 1000000000)))
    print(time.perf_counter() - start)