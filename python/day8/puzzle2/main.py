from min_steps import min_steps, parse_input
import time


if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        in_str = f.read()
    start = time.perf_counter()
    pi = parse_input(in_str)
    print(time.perf_counter() - start)
    print(min_steps(pi[1], pi[0]))