# I get 1582331846365 instead of 1566786613613
# I must have missed 1 edge case but I don't have the courage to find it

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

def possible_positions(springs, min_size):
    """
    Returns the possible groups of unknown springs that can contain min_size damaged springs in a row.
    Also includes the position of the first block of damaged springs.
    The output is a list of areas, each area being represented by a list of its positions. 
    [[area1_pos1, area1_pos2, ...], [area2_pos1, area2_pos2, ...], ...]
    """
    unknown_groups_positions = []
    current_group_unknowns = []
    first_damaged_spring = -1
    if springs[0] == '#':
        first_damaged_spring = 0
    else:
        for i, c in enumerate(springs):
            if i + 1 < len(springs) and springs[i+1] == '#':
                # Next spring is damaged : current spring must be left as a separation between groups
                first_damaged_spring = i + 1
                break
            if c == '?':
                current_group_unknowns.append(i)
            else:
                if len(current_group_unknowns) >= min_size:
                    unknown_groups_positions.append(current_group_unknowns)
                current_group_unknowns = []
    
    # Treating the last unknown group
    if len(current_group_unknowns) >= min_size:
        unknown_groups_positions.append(current_group_unknowns)

    # Adding all the positions associated with all the unknown groups
    possible_positions = []
    for group in unknown_groups_positions:
        for i in range(len(group) - min_size + 1):
            possible_positions.append(group[i:i+min_size])

    # Treating the first damaged block
    if first_damaged_spring == -1:
        # No damaged spring
        return possible_positions
    else:
        damaged_springs = [first_damaged_spring]
        i = first_damaged_spring + 1
        while i < len(springs) and springs[i] == '#':
            damaged_springs.append(i)
            i += 1
        if len(damaged_springs) > min_size:
            return possible_positions
        
        # Looking for unknown or damaged springs thats could extend the damaged block
        damaged_springs_extended = damaged_springs[:]

        # Checking the right side of the damaged block
        springs_to_check = min_size - len(damaged_springs)
        i = damaged_springs[-1] + 1
        while springs_to_check > 0 and i < len(springs) and springs[i] in '#?':
            springs_to_check -= 1
            damaged_springs_extended.append(i)
            i += 1
         
        # Checking the left side of the damaged block
        springs_to_check = min_size - len(damaged_springs)
        i = damaged_springs[0] - 1
        while springs_to_check > 0 and i >= 0 and springs[i] in '#?':
            springs_to_check -= 1
            damaged_springs_extended.insert(0, i)
            i -= 1

        # Checking if the area for the damaged block is separated from the next damaged block
        if damaged_springs_extended[-1] + 1 < len(springs) and springs[damaged_springs_extended[-1] + 1] == '#':
            # The damaged block is too big and would join another block
            # We need to remove the springs until the damaged block is separated from the next damaged block
            while springs[damaged_springs_extended[-1] + 1] == '#':
                damaged_springs_extended.pop()

        # Adding the valid positions associated with the damaged block to the list of possible positions
        for i in range(len(damaged_springs_extended) - min_size + 1):
            if damaged_springs_extended[i] - 1 >= 0 and springs[damaged_springs_extended[i] - 1] == '#':
                # The left side of the damaged block is connected to another block
                continue
            if damaged_springs_extended[i + min_size - 1] + 1 < len(springs) and springs[damaged_springs_extended[i + min_size - 1] + 1] == '#':
                # The right side of the damaged block is connected to another block
                continue
            possible_positions.append(damaged_springs_extended[i:i+min_size])

    return possible_positions

def positions_of_first_damaged_block(row):
    springs = row[0]
    block_positions = []
    for i, s in enumerate(springs):
        if s in '?.' and len(block_positions) != 0:
            return block_positions
        if s == '#':
            block_positions.append(i)
    return block_positions

def damage_arrangements_rec(row, memo):
    springs = row[0]
    damages = row[1]
    
    if len(springs) < sum(damages):
        # Base case
        return 0

    if len(damages) == 1:
        # Base case
        return len(possible_positions(springs, damages[0]))
    
    else:
        # Recursive case
        nb_arrangements = 0
        # Find all the possible positions of the actual first damage block
        first_block_size = damages[0]
        if springs == []:
            print(damages)
        possible_pos = possible_positions(springs, first_block_size)
        # print('\n\n\n')
        # print(''.join(springs), damages)
        for pos in possible_pos:
            # print(pos)
            # print(''.join(springs[pos[-1]+2:]))
            # print()
            # Position is valid, we can 'place' the first block and recurse on the rest of the row
            memo_key = (''.join(springs[pos[-1]+2:]), tuple(damages[1:]))
            if memo_key not in memo:
                memo[memo_key] = damage_arrangements_rec((springs[pos[-1]+2:], damages[1:]), memo)
            nb_arrangements += memo[memo_key]
        return nb_arrangements
    
def damage_arrangements(row):
    memo = {}
    return damage_arrangements_rec(row, memo)


if __name__ == '__main__':
    rows = parse_input('???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1')  
    # print(rows)

    # print('##?#?#?#?#?')
    # print(possible_positions('##?#?#?#?#?', 2))

    # print('?#?##?###')
    # print(possible_positions('?#?##?###', 4))
    # print('##?##????')
    # print(possible_positions('##?##????', 4))

    for row in rows:
        print(''.join(row[0]))
        print(damage_arrangements(row))