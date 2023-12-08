from min_steps import min_steps, parse_input


if __name__ == '__main__':
    with open('my_input.txt', 'r') as f:
        in_str = f.read()
    pi = parse_input(in_str)
    print(min_steps(pi[1], pi[0]))