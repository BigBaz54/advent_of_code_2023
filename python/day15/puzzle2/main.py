from focusing_power import parse_input, focusing_power
import time


if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        input_str = f.read()
    steps = parse_input(input_str)
    start = time.perf_counter()
    print(focusing_power(steps))
    print(time.perf_counter() - start)