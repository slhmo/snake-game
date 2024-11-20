import random

game_plain = []

def get_dimensions(num_rows = 4, num_columns = 4):
    i = 0
    while i<1:
        try:
            num_rows, num_columns = map(int, input('enter rows and columns: ').split())
            i += 1
        except ValueError:
            print('wrong input try again.')
        except NameError:
            print('wrong input try again.')
    return [num_rows, num_columns]


def make_game_plain(rows, columns):
    for i in range(rows):
        game_plain.append([])
        for j in range(columns):
            game_plain[i].append('.')
    i, j = random.randrange(0, rows), random.randrange(0, columns)
    game_plain[i][j] = 'x'


dimensions = get_dimensions()
make_game_plain(rows = dimensions[0], columns = dimensions[1])
print(game_plain)
