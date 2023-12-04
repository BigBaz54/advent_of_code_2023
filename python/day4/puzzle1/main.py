from winning_numbers import winning_numbers, parse_input

if __name__ == '__main__':
    with open('my_input.txt') as f:
        inp = f.read()
    numbers = parse_input(inp)
    s = 0
    for winning, my in numbers:
        # print(winning, my)
        # print(winning_numbers(my, winning))
        s += 2**(len(winning_numbers(my, winning))-1) if len(winning_numbers(my, winning)) > 0 else 0
    print(s)