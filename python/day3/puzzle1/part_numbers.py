def is_symbol(c):
    return (not c.isdigit()) and (not c == '.')

def part_numbers(one_line, previous_line, next_line):
    """
    Extract part numbers from the line
    # Working but unreadable
    """
    part_numbers_list = []
    current_number = ''
    current_number_pos = []
    for i in range(0, len(one_line)):
        if one_line[i].isdigit():
            # a digit of a possible part number
            current_number += one_line[i]
            current_number_pos.append(i)
            if i == len(one_line) - 1:
                # the last character of the line is a digit (could be a part number)
                first_digit_pos = current_number_pos[0]
                last_digit_pos = current_number_pos[-1]

                first_pos_to_check = first_digit_pos - 1 if first_digit_pos > 0 else 0
                last_pos_to_check = len(one_line) - 1

                for j in range(first_pos_to_check, last_pos_to_check + 1):
                    # checking above and below and in the left corners
                    if is_symbol(previous_line[j]) or is_symbol(next_line[j]):
                        part_numbers_list.append(int(current_number))
                        current_number = ''
                        current_number_pos = []
                        break
        else:
            # reset the buffer
            if current_number == '':
                # nothing is in the buffer, continue
                continue
            elif is_symbol(one_line[i]):
                # a current number, followed by a symbol : a part number
                part_numbers_list.append(int(current_number))
                current_number = ''
                current_number_pos = []
                continue
            else:
                # a current number, followed by a '.'
                first_digit_pos = current_number_pos[0]
                last_digit_pos = current_number_pos[-1]

                first_pos_to_check = first_digit_pos - 1 if first_digit_pos > 0 else 0
                last_pos_to_check = last_digit_pos + 1 if last_digit_pos < len(one_line) - 1 else len(one_line) - 1

                for j in range(first_pos_to_check, last_pos_to_check + 1):
                    # checking above and below and in the corners
                    if is_symbol(previous_line[j]) or is_symbol(next_line[j]):
                        part_numbers_list.append(int(current_number))
                        current_number = ''
                        current_number_pos = []
                        break
                
                if (i>0 and is_symbol(one_line[first_digit_pos-1]) and current_number != ''):
                    # checking to the left
                    part_numbers_list.append(int(current_number))
                    current_number = ''
                    current_number_pos = []
                    continue
                
                current_number = ''
                current_number_pos = []

    return part_numbers_list

def parse_input(list_of_lines):
    """
    Parse the input into a list of LINES.
    Each LINE is a tuple of 2 lists: 
    - the first list is a list of tuples containing : the integer and the positions of the number (as a list of integers),
    - the second list of the positions of the symbols (as a list of integers).
    """
    parsed_lines = []
    for line in list_of_lines:
        input_line = line.strip()
        numbers = []
        symbols = []
        current_number = ''
        current_number_pos = []
        for i, c in enumerate(input_line):
            if is_symbol(c):
                symbols.append(i)
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
        parsed_lines.append((numbers, symbols))
    return parsed_lines

def part_numbers2(one_line, previous_line, next_line):
    """
    Extract part numbers from the line.
    :param one_line: the current line's positions of the numbers and symbols returned by parse_input()
    :param previous_line: the previous line's positions of the numbers and symbols returned by parse_input()
    :param next_line: the next line's positions of the numbers and symbols returned by parse_input()
    :return: a list of the part numbers of the line
    """
    part_numbers_list = []
    symbols_pos = one_line[1]
    previous_symbols_pos = previous_line[1]
    next_symbols_pos = next_line[1]
    is_part_number = False
    for number, number_pos in one_line[0]:
        # number is an integer
        # number_pos is a list of integers
        first_digit_pos = number_pos[0]
        last_digit_pos = number_pos[-1]

        first_pos_to_check = first_digit_pos - 1 if first_digit_pos > 0 else 0
        last_pos_to_check = last_digit_pos + 1

        for j in range(first_pos_to_check, last_pos_to_check + 1):
            # checking above and below and in the corners
            if j in previous_symbols_pos or j in next_symbols_pos:
                is_part_number = True
                break

        if (first_digit_pos > 0 and first_digit_pos - 1 in symbols_pos) and not is_part_number:
            # checking to the left
            is_part_number = True

        if (last_digit_pos + 1 in symbols_pos) and not is_part_number:
            # checking to the right
            is_part_number = True

        if is_part_number:
            part_numbers_list.append(number)
            is_part_number = False

    return part_numbers_list

    

if __name__ == '__main__':
    print(part_numbers('**35*633**', '**********', '**********'))
    pi = parse_input(['**35*633**', '**********', '**********'])
    print(part_numbers2(pi[0], pi[1], pi[2]))
    print(part_numbers('............../....94................414......18.............................861....*.....878..........24@.............875=.693*320..864.989', '...............646........&..$.........*...................542....................................370......686.567..........................', '...................*.........665..............*...595..........201......738..+...784..187....*237..../..............................*......*'))
    pi = parse_input(['............../....94................414......18.............................861....*.....878..........24@.............875=.693*320..864.989', '...............646........&..$.........*...................542....................................370......686.567..........................', '...................*.........665..............*...595..........201......738..+...784..187....*237..../..............................*......*'])
    print(part_numbers2(pi[0], pi[1], pi[2]))

