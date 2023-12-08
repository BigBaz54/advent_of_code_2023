def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    instr = lines[0]
    nodes = {}
    for line in lines[2:]:
        origin = line.split(' = ')[0]
        dest = line.split(', ')
        left = dest[0][-3:]
        right = dest[1][:3]
        nodes[origin] = (left, right)
    return instr, nodes

def reach_ZZZ_rec(nodes, start, instr, base_start, base_instr, current_step):
    """
    Ends without returning anything for some reason
    """
    print(current_step)
    # print(instr)
    # print(start)
    if start == 'ZZZ':
        return current_step
    if instr[0] == 'R':
        return reach_ZZZ_rec(nodes, nodes[start][1], instr[1:] if len(instr)>=2 else base_instr, base_start, base_instr, current_step + 1)
    else:
        return reach_ZZZ_rec(nodes, nodes[start][0], instr[1:] if len(instr)>=2 else base_instr, base_start, base_instr, current_step + 1)

def min_steps(nodes, instr):
    base_instr = instr
    start = 'AAA'
    steps = 0
    while start != 'ZZZ':
        if instr == '':
            instr = base_instr
        if instr[0] == 'L':
            start = nodes[start][0]
        else:
            start = nodes[start][1]
        instr = instr[1:]
        steps += 1
    return steps


if __name__ == '__main__':
    # pi = parse_input('RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)')
    pi = parse_input('LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)')
    print(min_steps(pi[1], pi[0]))