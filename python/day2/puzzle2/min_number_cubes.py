def is_possible_game(game, red, green, blue):
    """
    Return True if game is a possible game, False otherwise.
    :param game: a game (list of tuples (red, green, blue))
    :param red: number of red cubes available
    :param green: number of green cubes available
    :param blue: number of blue cubes available
    """
    for (r, g, b) in game:
        if r > red or g > green or b > blue:
            return False
    return True

def parse_input():
    """
    Parse input into a list of games. Each game is a list of tuples (red, green, blue).
    """
    games = []
    with open('my_input.txt') as f:
        lines = f.readlines()
    for line in lines:
        actual_line = line.split(': ')[1].strip()
        game = []
        for draw in actual_line.split('; '):
            game.append((0,0,0))
            for cubes in draw.split(', '):
                if cubes.split(' ')[1] == 'red':
                    game[-1] = (int(cubes.split(' ')[0]), game[-1][1], game[-1][2])
                elif cubes.split(' ')[1] == 'green':
                    game[-1] = (game[-1][0], int(cubes.split(' ')[0]), game[-1][2])
                elif cubes.split(' ')[1] == 'blue':
                    game[-1] = (game[-1][0], game[-1][1], int(cubes.split(' ')[0]))
        games.append(game)
    return games

def min_number_cubes(game):
    """
    Return the minimum number of cubes needed to make the game possible.
    :param game: a game (list of tuples (red, green, blue))
    """
    min_red = 0
    min_green = 0
    min_blue = 0
    for (r, g, b) in game:
        if r > min_red:
            min_red = r
        if g > min_green:
            min_green = g
        if b > min_blue:
            min_blue = b
    return (min_red, min_green, min_blue)


if __name__ == '__main__':
    games = parse_input()
    sum = 0
    for game in games:
        red, green, blue = min_number_cubes(game)
        sum += red * green * blue
    print(sum)
    