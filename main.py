lives = 3

class Player:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

def insertposition(player_position_x, grid_array):
    grid_array.remove(0)
    grid_array.insert(player_position_x - 1, 1)
    return grid_array


Jake = Player(1, 10, 'Jake')
David = Player(1, 10, 'David')

firstgridarray  = [0, 0, 0, 0, 0, 0]
secondgridarray = [0, 0, 0, 0, 0, 0]
thirdgridarray  = [0, 0, 0, 0, 0, 0]
fourthgridarray = [0, 0, 0, 0, 0, 0]
fifthgridarray  = [0, 0, 0, 0, 0, 0]
sixthgridarray  = [0, 0, 0, 0, 0, 0]

Jake.x = 3
firstgridarray = insertposition(Jake.x, firstgridarray)

print("{}\n{}\n{}\n{}\n{}\n{}\n".format(
    firstgridarray, secondgridarray, thirdgridarray,
    fourthgridarray, fifthgridarray, sixthgridarray
))

