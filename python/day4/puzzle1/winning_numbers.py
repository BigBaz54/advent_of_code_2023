def winning_numbers(my_numbers, winning_numbers):
    my_numbers = set(my_numbers)
    winning_numbers = set(winning_numbers)
    return my_numbers.intersection(winning_numbers)

def parse_input(input):
    numbers = []
    for line in input.splitlines():
        line = line.strip().split(': ')[1]
        winning_str = line.split(' | ')[0]
        my_str = line.split(' | ')[1]
        winning_numbers = winning_str.split('  ')
        my_numbers = my_str.split('  ')
        winning_numbers_parsed = []
        for n in winning_numbers:
            l = n.split(' ')
            winning_numbers_parsed += l
        my_numbers_parsed = []
        for n in my_numbers:
            l = n.split(' ')
            my_numbers_parsed += l
        winning_numbers_parsed = [int(n) for n in winning_numbers_parsed if n != '']
        my_numbers_parsed = [int(n) for n in my_numbers_parsed if n != '']
        numbers.append((winning_numbers_parsed, my_numbers_parsed))
    return numbers

if __name__ == '__main__':
    pi = parse_input("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    print(pi)