import time
import keyboard

firstgridarray  = [0, 0, 0, 0, 0, 0]
secondgridarray = [0, 0, 0, 0, 0, 0]
thirdgridarray  = [0, 0, 0, 0, 0, 0]
fourthgridarray = [0, 0, 0, 0, 0, 0]
fifthgridarray  = [0, 0, 0, 0, 0, 0]
sixthgridarray  = [0, 0, 0, 0, 0, 0]

class Player:

    def __init__(self, x, y, name, lives):
        self.x = x
        self.y = y
        self.name = name
        self.lives = lives
    
    def movex(self, posx, grid_array):
        self.x.append(posx)
        grid_array.remove(1)
        grid_array(posx - 1, 1)

    def spawn(self, spawn_row):
        spawn_row.pop(self.x - 1)
        spawn_row.insert(self.x - 1, 1)

    def die(self):
        print(self.name + " has died!")

def insertpos(player_position_x, prev_pos, grid_array):
    grid_array.pop(player_position_x - 1)
    grid_array.insert(player_position_x - 1, 1)
    grid_array.pop(prev_pos - 1)
    grid_array.insert(prev_pos - 1, 0)

    return grid_array

def insertpos2(posx, prev_pos, grid_array):
    grid_array.pop(posx - 1)
    grid_array.insert(posx - 1, 1)

    return grid_array

def deletepos(posx, grid_array):
    grid_array.pop(posx - 1)
    grid_array.insert(posx - 1, 0)

    return grid_array

Jake = Player(3, 1, 'Jake', 3)

begin = input("Begin? Y/N")
if (begin == 'Y'):
    GameRunning = True
    Jake.spawn(firstgridarray)
    print("{}\n{}\n{}\n".format(
        firstgridarray, secondgridarray, thirdgridarray
    ))

while GameRunning == True:
    prev_pos = Jake.x
    
    if (Jake.lives < 1):
        Jake.die()
    
    key = keyboard.read_key()
    if key == 'd':
        Jake.x = Jake.x + 1
        if Jake.y == 1:
            firstgridarray = insertpos(Jake.x, prev_pos, firstgridarray)
        if Jake.y == 2:
            secondgridarray = insertpos(Jake.x, prev_pos, secondgridarray)
        if Jake.y == 3:
            thirdgridarray = insertpos(Jake.x, prev_pos, thirdgridarray)
        if Jake.y == 4:
            fourthgridarray = insertpos(Jake.x, prev_pos, fourthgridarray)
        if Jake.y == 5:
            fifthgridarray = insertpos(Jake.x, prev_pos, fifthgridarray)
    
    if key == 'a':
        Jake.x = Jake.x - 1
        if Jake.y == 1:
            firstgridarray = insertpos(Jake.x, prev_pos, firstgridarray)
        if Jake.y == 2:
            secondgridarray = insertpos(Jake.x, prev_pos, secondgridarray)
        if Jake.y == 3:
            thirdgridarray = insertpos(Jake.x, prev_pos, thirdgridarray)
        if Jake.y == 4:
            fourthgridarray = insertpos(Jake.x, prev_pos, fourthgridarray)
        if Jake.y == 5:
            fifthgridarray = insertpos(Jake.x, prev_pos, fifthgridarray)

    if key == 's':

        if Jake.y == 1:
            firstgridarray = deletepos(Jake.x, firstgridarray)
        if Jake.y == 2:
            secondgridarray = deletepos(Jake.x, secondgridarray)
        if Jake.y == 3:
            thirdgridarray = deletepos(Jake.x, thirdgridarray)
        if Jake.y == 4:
            fourthgridarray = deletepos(Jake.x, fourthgridarray)
        if Jake.y == 5:
            fifthgridarray = deletepos(Jake.x, fifthgridarray)

        Jake.y = Jake.y + 1

        if Jake.y == 1:
            firstgridarray = insertpos2(Jake.x, prev_pos, firstgridarray)
        if Jake.y == 2:
            secondgridarray = insertpos2(Jake.x, prev_pos, secondgridarray)
        if Jake.y == 3:
            thirdgridarray = insertpos2(Jake.x, prev_pos, thirdgridarray)
        if Jake.y == 4:
            fourthgridarray = insertpos2(Jake.x, prev_pos, fourthgridarray)
        if Jake.y == 5:
            fifthgridarray = insertpos2(Jake.x, prev_pos, fifthgridarray)
    
    if key == 'w':

        if Jake.y == 1:
            firstgridarray = deletepos(Jake.x, firstgridarray)
        if Jake.y == 2:
            secondgridarray = deletepos(Jake.x, secondgridarray)
        if Jake.y == 3:
            thirdgridarray = deletepos(Jake.x, thirdgridarray)
        if Jake.y == 4:
            fourthgridarray = deletepos(Jake.x, fourthgridarray)
        if Jake.y == 5:
            fifthgridarray = deletepos(Jake.x, fifthgridarray)

        Jake.y = Jake.y - 1

        if Jake.y == 1:
            firstgridarray = insertpos2(Jake.x, prev_pos, firstgridarray)
        if Jake.y == 2:
            secondgridarray = insertpos2(Jake.x, prev_pos, secondgridarray)
        if Jake.y == 3:
            thirdgridarray = insertpos2(Jake.x, prev_pos, thirdgridarray)
        if Jake.y == 4:
            fourthgridarray = insertpos2(Jake.x, prev_pos, fourthgridarray)
        if Jake.y == 5:
            fifthgridarray = insertpos2(Jake.x, prev_pos, fifthgridarray)
    
    print("{}\n{}\n{}\n{}\n{}".format(
        firstgridarray, secondgridarray, thirdgridarray, fourthgridarray, fifthgridarray
    ))
    print(Jake.y)
    time.sleep(0.5)
