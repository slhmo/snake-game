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
    for i1 in range(rows):
        game_plain.append([])
        for j1 in range(columns):
            game_plain[i1].append('.')
    i1, j1 = random.randrange(0, rows), random.randrange(0, columns)
    game_plain[i1][j1] = 'X'
    return [i1, j1]

dimensions = get_dimensions()
head_position = (
    make_game_plain(rows = dimensions[0], columns = dimensions[1])[0:2]
)

for i2 in game_plain:
    print(i2)
print(head_position)

def move_maker():
    move = input("choose('w', 's', 'd', 'a'): ")

    if move == 'w':
        i = 0
        tmp = game_plain[0][head_position[1]]
        while i<len(game_plain)-1:
            game_plain[i][head_position[1]] = game_plain[i+1][head_position[1]]
            i += 1
        game_plain[len(game_plain)-1][head_position[1]] = tmp

    if move == 's':
        i = len(game_plain)-1
        tmp = game_plain[len(game_plain)-1][head_position[1]]
        while i>0:
            game_plain[i][head_position[1]] = game_plain[i-1][head_position[1]]
            i -= 1
        game_plain[0][head_position[1]] = tmp

    if move == 'a':
        if head_position[1] == 0:
            print('you lost!')
        else:
            j = 0
            tmp = game_plain[head_position[0]][0]
            while j < len(game_plain[0])-1:
                game_plain[head_position[0]][j] = game_plain[head_position[0]][j+1]
                j += 1
            game_plain[head_position[0]][len(game_plain[0]) - 1] = tmp

    if move == 'd':
        if head_position[1] == 0:
            print('you lost!')
        else:
            j = len(game_plain[0])-1
            tmp = game_plain[head_position[0]][len(game_plain[0])-1]
            while j > 0:
                game_plain[head_position[0]][j] = game_plain[head_position[0]][j-1]
                j -= 1
            game_plain[head_position[0]][0] = tmp


move_maker()
for i2 in game_plain:
    print(i2)
