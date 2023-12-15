def parse_input(input_str):
    input_str = input_str.strip()
    steps = input_str.split(',')
    return steps

def hash(seq):
    current_value = 0
    for c in seq:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


if __name__ == '__main__':
    input_str = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
    steps = parse_input(input_str)
    for step in steps:
        print(hash(step))