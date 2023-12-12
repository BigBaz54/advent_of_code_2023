import itertools

def parse_input(input_str):
    lines = input_str.splitlines()
    lines = [line.strip() for line in lines]
    rows = []
    for line in lines:
        row = line.split(' ')
        springs = row[0]
        damages = row[1]
        damages = damages.split(',')
        # Unfolding the records
        damages = [int(damage) for damage in damages]*5
        springs =( list(springs)+['?'])*5
        springs.pop()
        rows.append((springs, damages))
    return rows

def large_enough_groups_of_unknown_before_first_damaged(row, min_size):
    groups_positions = []
    current_group = []
    for i, c in enumerate(row[0]):
        if c == '#':
            if len(current_group) >= min_size:
                groups_positions.append(current_group)
            return groups_positions
        if c == '?':
            current_group.append(i)
        else:
            if len(current_group) >= min_size:
                groups_positions.append(current_group)
            current_group = []
    return groups_positions

def positions_of_first_damaged_block(row):
    springs = row[0]
    block_positions = []
    for i, s in enumerate(springs):
        if s in '?.' and len(block_positions) != 0:
            return block_positions
        if s == '#':
            block_positions.append(i)
    return block_positions

def damage_arrangements(row):
    springs = row[0]
    damages = row[1]
    if len(damages) == 1:
        # Base case
        if len(springs) < damages[0]:
            return 0
        else:
            return len(list(itertools.combinations(range(len(springs)), damages[0])))
    else:
        # Recursive case
        nb_arrangements = 0
        # Find all the possible positions of the actual first damage block
        first_block_size = damages[0]
        possible_positions = []
        first_damaged_block_current_positions = positions_of_first_damaged_block(row)
        max_end_position = first_damaged_block_current_positions[0] if len(first_damaged_block_current_positions) > 0 else len(springs) - 1
        for i in range(max_end_position+1):
            possible_positions.append(list(range(i, i+first_block_size)))
        for pos in possible_positions:
            # Check is the position for the first block is valid
            if '.' in [springs[p] for p in pos if p < len(springs)]:
                # At least one spring can't be damaged
                continue
            if pos[-1] >= len(springs):
                # The first block doesn't fit in the row
                continue
            if set(pos).intersection(set(first_damaged_block_current_positions)) != set():
                # Completing the first block with the current damaged springs
                if set(pos + first_damaged_block_current_positions) != set(pos):
                    # The completed block is too big
                    continue
            if len(springs) > pos[-1] + 1 and springs[pos[-1]+1] == '#':
                # The first block is to big and would join another block
                continue
            # Position is valid, we can 'place' the first block and recurse on the rest of the row
            nb_arrangements += damage_arrangements((springs[pos[-1]+2:], damages[1:]))
        return nb_arrangements


if __name__ == '__main__':
    rows = parse_input('???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1')  
    # print(rows)
    # print(number_of_damaged_springs(rows[0]))
    # print(is_row_valid('#.#.###', [1,1,3]))
    # print(is_row_valid('##..###', [1,1,2]))
    # print(''.join(rows[0][0]))
    # print(damage_arrangements(rows[0]))
    # print(large_enough_groups_of_unknown_before_first_damaged((rows[-1][0][4:], rows[-1][1]), 2))
    # print(positions_of_first_damaged_block(rows[-1]))
    print(''.join(rows[-1][0]))
    print(damage_arrangements(rows[-1]))
