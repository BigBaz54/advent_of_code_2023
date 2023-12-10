from farthest_point_in_loop import parse_input, farthest_point_in_loop


if __name__ == '__main__':
    with open('my_input.txt') as f:
        in_str = f.read()
    pipes_map = parse_input(in_str)
    print(farthest_point_in_loop(pipes_map))