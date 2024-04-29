import time
import keyboard

firstgridarray  = [0, 0, 0, 0, 0, 0]
secondgridarray = [0, 0, 0, 0, 0, 0]
thirdgridarray  = [0, 0, 0, 0, 0, 0]
fourthgridarray = [0, 0, 0, 0, 0, 0]
fifthgridarray  = [0, 0, 0, 0, 0, 0]
sixthgridarray  = [0, 0, 0, 0, 0, 0]

class Player:
    
    lives = 3

    def __init__(self, x, y, name):
        self.x = x
        self.z = y
        self.name = name
    
    def movex(self, posx, grid_array):
        self.x.append(posx)
        grid_array.remove(0)
        grid_array(posx - 1, 1)

    def die(self):
        print(self.name + " has died!")

def insertpos(player_position_x, grid_array):
    grid_array.remove(0)
    grid_array.insert(player_position_x - 1, 1)
    return grid_array

def keyautoload():
    key = keyboard.read_key()
    if key == 'd':
        print('d')
    if key == 'a':
        print('a')

Jake = Player(1, 2, 'Jake')

x = True

while x == True:
    Jake.x = Jake.x + 1
    firstgridarray = insertpos(Jake.x, firstgridarray)
    print("{}\n{}\n{}\n{}\n{}\n{}\n".format(
        firstgridarray, secondgridarray, thirdgridarray,
        fourthgridarray, fifthgridarray, sixthgridarray
        ))

time.sleep(0.1)

