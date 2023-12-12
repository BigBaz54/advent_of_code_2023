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
        damages = [int(damage) for damage in damages]
        rows.append((springs, damages))
    return rows

def number_of_damaged_springs(row):
    return len([c for c in row[0] if c == '#'])

def positions_of_unknown_springs(row):
    pos = []
    for i in range(len(row[0])):
        if row[0][i] == '?':
            pos.append(i)
    return pos

def is_row_valid(springs, damages):
    current_damages_blocks = []
    current_block_damage = 0
    for s in springs:
        if s == '#':
            current_block_damage += 1
        else:
            if current_block_damage > 0:
                current_damages_blocks.append(current_block_damage)
            current_block_damage = 0
    if current_block_damage > 0:
        current_damages_blocks.append(current_block_damage)
    return current_damages_blocks == damages

def damage_arrangements(row):
    springs = row[0]
    damages = row[1]
    current_damages = number_of_damaged_springs(row)
    total_damages = sum(damages)
    damages_left = total_damages - current_damages
    unknown_springs_pos = positions_of_unknown_springs(row)
    arrangements = itertools.combinations(list(range(len(unknown_springs_pos))), damages_left)
    valid_arrangements = 0
    for arrangement in arrangements:
        springs_copy = list(springs)
        for spring_to_damage in list(arrangement):
            springs_copy[unknown_springs_pos[spring_to_damage]] = '#'
        if is_row_valid(springs_copy, damages):
            valid_arrangements += 1
    return valid_arrangements


if __name__ == '__main__':
    rows = parse_input('???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1')  
    # print(rows)
    # print(number_of_damaged_springs(rows[0]))
    # print(is_row_valid('#.#.###', [1,1,3]))
    # print(is_row_valid('##..###', [1,1,2]))
    print(damage_arrangements(rows[0]))
    print(damage_arrangements(rows[-1]))
