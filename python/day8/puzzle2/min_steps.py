import math


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

def min_steps(nodes, instr):
    base_instr = instr
    steps = 0
    min_steps = []
    starting_nodes = [node for node in nodes if node[2] == 'A']
    for starting_node in starting_nodes:
        while not starting_node.endswith('Z'):
            if instr == '':
                instr = base_instr
            if instr[0] == 'L':
                starting_node = nodes[starting_node][0]
            else:
                starting_node = nodes[starting_node][1]
            instr = instr[1:]
            steps += 1
        min_steps.append(steps)
        steps = 0
    return math.lcm(*min_steps)


if __name__ == '__main__':
    # pi = parse_input('RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)')
    pi = parse_input('LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)')
    print(min_steps(pi[1], pi[0]))