import character

player = character.Character(0, 0, 5, 10, 1000)

X = "nothing"
M = "monster"
C = "chest"
B = "boss"



rooms = [["X","X","M","X","M","C","C"],
         ["M","X","X","M","X","X","C"],
         ["X","C","X","X","M","X","X"],
         ["X","X","C","X","C","X","X"],
         ["C","X","X","M","X","X","M"],
         ["X","X","B","X","X","M","M"],
         ["M","M","X","X","M","M","B"],
        ]

def get_room(x,y):
    return rooms[y][x]

def update_room():
    rooms[player.y_pos][player.x_pos] = ' '


def current_room():
    rooms[player.y_pos][player.x_pos] = 'o'
    for rows in rooms:
        for space in rows:
            print(space, end='  ')
        print()

