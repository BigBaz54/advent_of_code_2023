def parse_input(input_str):
    input_str = input_str.strip()
    steps = input_str.split(',')
    steps2 = []
    for s in steps:
        if '=' in s:
            steps2.append((s.split('=')[0], s[-2:]))
        else:
            steps2.append((s.split('-')[0], s[-1]))
    return steps2

def hash(seq):
    current_value = 0
    for c in seq:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

def focusing_power(steps):
    boxes = {n: [] for n in range(256)}
    for step in steps:
        if step[1] == '-':
            box_num = hash(step[0])
            lens = boxes[box_num]
            for label, focal in lens:
                if label == step[0]:
                    lens.remove([label, focal])
                    break
        else:
            box_num = hash(step[0])
            lens = boxes[box_num]
            new_focal = int(step[1][-1])
            for one_lens in lens:
                if one_lens[0] == step[0]:
                    one_lens[1] = new_focal
                    break
            else:
                lens.append([step[0], new_focal])
    s = 0
    for box_num, lens in boxes.items():
        for i, (label, focal) in enumerate(lens):
            s += (box_num + 1) * (i + 1) * focal
    return s


if __name__ == '__main__':
    input_str = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
    steps = parse_input(input_str)
    print(focusing_power(steps))