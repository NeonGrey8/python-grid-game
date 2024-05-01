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
        grid_array.remove(1)
        grid_array(posx - 1, 1)

    def spawn(self, spawn_row):
        spawn_row.pop(self.x - 1)
        spawn_row.insert(self.x - 1, 1)

    def die(self):
        print(self.name + " has died!")

def insertpos(player_position_x, prev_position, grid_array):
    grid_array.pop(player_position_x - 1)
    grid_array.insert(player_position_x - 1, 1)
    grid_array.pop(prev_pos - 1)
    grid_array.insert(prev_pos - 1, 0)

    return grid_array

def key_handler(posx):
    key = keyboard.read_key()
    if key == 'd':
        posx = posx + 1
    if key == 'a':
        posx = posx - 1

Jake = Player(3, 1, 'Jake')
begin = input("Begin? Y/N")
if (begin == 'Y'):
    GameRunning = True

Jake.spawn(firstgridarray)

while GameRunning == True:
    prev_pos = Jake.x

    key = keyboard.read_key()
    if key == 'd':
        Jake.x = Jake.x + 1
        firstgridarray = insertpos(Jake.x, prev_pos, firstgridarray)
    if key == 'a':
        Jake.x = Jake.x - 1
        firstgridarray = insertpos(Jake.x, prev_pos, firstgridarray)
    #if key == 's':
    #    Jake.y = Jake.y + 1
    
    #if (Jake.y == 1):
    #    firstgridarray
    print("{}\n{}\n{}\n{}\n{}\n{}\n".format(
        firstgridarray, secondgridarray, thirdgridarray,
        fourthgridarray, fifthgridarray, sixthgridarray
        ))
    time.sleep(0.5)
