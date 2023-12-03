def parse_input(list_of_lines):
    """
    Parse the input into a list of LINES.
    Each LINE is a tuple of 2 lists: 
    - the first list is a list of tuples containing : the integer and the positions of the number (as a list of integers),
    - the second list of the positions of the gears (as a list of integers).
    """
    parsed_lines = []
    for line in list_of_lines:
        input_line = line.strip()
        numbers = []
        gears = []
        current_number = ''
        current_number_pos = []
        for i, c in enumerate(input_line):
            if c == '*':
                gears.append(i)
            if c.isdigit():
                current_number += c
                current_number_pos.append(i)
                if i == len(input_line) - 1:
                    numbers.append((int(current_number), current_number_pos))
                    current_number = ''
                    current_number_pos = []
            else:
                if current_number != '':
                    numbers.append((int(current_number), current_number_pos))
                    current_number = ''
                    current_number_pos = []
        parsed_lines.append((numbers, gears))
    return parsed_lines

def gear_ratios(one_line, previous_line, next_line):
    """
    Extract gear ratios from a line.
    :param one_line: the current line's positions of the numbers and gears returned by parse_input()
    :param previous_line: the previous line's positions of the numbers and gears returned by parse_input()
    :param next_line: the next line's positions of the numbers and gears returned by parse_input()
    :return: a list of gear ratios
    """
    gear_ratios_list = []
    gear_pos = one_line[1]
    numbers = one_line[0]
    previous_numbers = previous_line[0]
    next_numbers = next_line[0]

    for gp in gear_pos:
        adjacent_numbers = []

        # find the adjacent numbers in the current line
        for n in numbers:
            # checking the left side of the gear
            if gp > 0 and gp - 1 in n[1]:
                adjacent_numbers.append(n[0])
                continue

            # checking the right side of the gear
            if gp + 1 in n[1]:
                adjacent_numbers.append(n[0])

        # find the adjacent numbers in the previous line and next line
        for n in previous_numbers + next_numbers:
            # checking the left corners
            if gp > 0 and gp - 1 in n[1]:
                adjacent_numbers.append(n[0])
                continue

            # checking above and below
            if gp in n[1]:
                adjacent_numbers.append(n[0])
                continue
            
            # checking the right corners
            if gp + 1 in n[1]:
                adjacent_numbers.append(n[0])

        # find out if the gear is actually a gear
        if len(adjacent_numbers) == 2:
            gear_ratios_list.append(adjacent_numbers[0] * adjacent_numbers[1])
            
    return gear_ratios_list


if __name__ == '__main__':
    pi = parse_input(['**35*633**', '**********', '**********'])
    print(gear_ratios(pi[0], pi[1], pi[2]))
    pi = parse_input(['............../....94................414......18.............................861....*.....878..........24@.............875=.693*320..864.989',
                      '...............646........&..$.........*...................542....................................370......686.567..........................',
                      '...................*.........665..............*...595..........201......738..+...784..187....*237..../..............................*......*'])
    print(gear_ratios(pi[0], pi[1], pi[2]))

