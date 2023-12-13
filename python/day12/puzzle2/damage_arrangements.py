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
        springs =(springs + '?')*5
        springs = springs[:-1]
        rows.append((springs, damages))
    return rows

def damage_arrangements_rec(row, memo):
    springs, damages = row
    
    # Base case
    if len(damages) == 0:
        # All damages have been placed
        return 1 if '#' not in springs else 0
    if sum(damages) + len(damages) - 1 > len(springs):
        # Not enough space for the damages groups split by at least one '.'
        return 0
    
    # Recursive case
    if springs[0] == '.':
        # If we start with a '.', we just remove it
        memo_key = (springs[1:], tuple(damages))
        if memo_key not in memo:
            memo[memo_key] = damage_arrangements_rec(memo_key, memo)
        return memo[memo_key]
    
    nb_arrangements = 0

    # Try to place a '.' instead of the '?'
    if springs[0] == '?':
        memo_key = (springs[1:], tuple(damages))
        if memo_key not in memo:
            memo[memo_key] = damage_arrangements_rec(memo_key, memo)
        nb_arrangements += memo[memo_key]

    # Try to place the first damages group as soon as possible
    springs_to_damage = springs[:damages[0]]
    if len(springs) < damages[0]:
        # If there is not enough space, we can't place the first damages group
        pass
    elif '.' in springs_to_damage:
        # If there is a '.', we can't place the first damages group
        pass
    elif len(springs) > damages[0] and springs[damages[0]] == '#':
        # There is a '#' just after the first damages group, we can't place it because we need at least one '.' between two damages groups
        pass
    else:
        # We can place the first damages group
        memo_key = (springs[damages[0]+1:], tuple(damages[1:]))
        if memo_key not in memo:
            memo[memo_key] = damage_arrangements_rec(memo_key, memo)
        nb_arrangements += memo[memo_key]

    return nb_arrangements

def damage_arrangements(row):
    memo = {}
    return damage_arrangements_rec(row, memo)

if __name__ == '__main__':
    rows = parse_input('???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1')  
    for row in rows:
        print(row[0])
        print(damage_arrangements(row))
        print()