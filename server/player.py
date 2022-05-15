import socket
from tabnanny import check
from threading import Thread
from random import randint
import time


def check_position(x, y, array, turn, size):
    flag = 0
    if turn == 1 and y+1 <= 10:  # vlevo
        if y - size+1 >= 0:
            for j in range(y-size+1, y+1):
                if(array[x][j] != 0):
                    flag = 2
        else:
            return 1  # ne vlez
    elif turn == 2 and x+1 <= 10:  # vverh
        if x - size + 1 >= 0:
            for j in range(x - size+1, x+1):
                if(array[j][y] != 0):
                    flag = 2
        else:
            return 1  # ne vlez
    elif turn == 3:  # vpravo
        if y + size <= 10:
            for j in range(y, y+size):
                if(array[x][j] != 0):
                    flag = 2
        else:
            return 1  # ne vlez
    if turn == 4:  # vniz
        if x + size <= 10:
            for i in range(x, x+size):
                if(array[i][y] != 0):
                    flag = 2
        else:
            return 1  # ne vlez
    return flag


def ships_put(array, x, y, turn, size):
    if turn == 1:  # vlevo
        for j in range(y-size+1, y+1):
            array[x][j] = 1
        if x - 1 >= 0:
            for j in range(y-size+1, y+1):
                if j >= 0 and j <= 9:
                    array[x-1][j] = 2
        if x + 1 <= 9:
            for j in range(y-size+1, y+1):
                if j >= 0 and j <= 9:
                    array[x+1][j] = 2
        if y - size >= 0:
            for j in range(x-1, x+2):
                if j >= 0 and j <= 9:
                    array[j][y-size] = 2
        if y + 1 <= 9:
            for j in range(x-1, x+2):
                if j >= 0 and j <= 9:
                    array[j][y+1] = 2
    if turn == 2:  # vverh
        for j in range(x - size+1, x+1):
            array[j][y] = 1
        if y - 1 >= 0:
            for j in range(x-size+1, x+1):
                if j >= 0 and j <= 9:
                    array[j][y-1] = 2
        if y + 1 <= 9:
            for j in range(x-size+1, x+1):
                if j >= 0 and j <= 9:
                    array[j][y+1] = 2
        if x - size >= 0:
            for j in range(y-1, y+2):
                if j >= 0 and j <= 9:
                    array[x-size][j] = 2
        if x + 1 <= 9:
            for j in range(y-1, y+2):
                if j >= 0 and j <= 9:
                    array[x+1][j] = 2
    if turn == 3:  # vpravo
        for j in range(y, y+size):
            array[x][j] = 1
        if x - 1 >= 0:
            for j in range(y, y+size):
                if j >= 0 and j <= 9:
                    array[x-1][j] = 2
        if x + 1 <= 9:
            for j in range(y, y+size):
                if j >= 0 and j <= 9:
                    array[x+1][j] = 2
        if y + size <= 9:
            for j in range(x-1, x+2):
                if j >= 0 and j <= 9:
                    array[j][y+size] = 2
        if y - 1 >= 0:
            for j in range(x-1, x+2):
                if j >= 0 and j <= 9:
                    array[j][y-1] = 2
    if turn == 4:  # vniz
        for j in range(x, x+size):
            array[j][y] = 1
        if y - 1 >= 0:
            for j in range(x, x+size):
                if j >= 0 and j <= 9:
                    array[j][y-1] = 2
        if y + 1 <= 9:
            for j in range(x, x+size):
                if j >= 0 and j <= 9:
                    array[j][y+1] = 2
        if x + size <= 9:
            for j in range(y-1, y+2):
                if j >= 0 and j <= 9:
                    array[x+size][j] = 2
        if x - 1 >= 0:
            for j in range(y-1, y+2):
                if j >= 0 and j <= 9:
                    array[x-1][j] = 2


def generate_ships(array, count, size, count_ship):
    if count < count_ship:
        position_x = randint(0, 9)
        position_y = randint(0, 9)
        if size > 1:
            turn = randint(1, 4)  # 1-vlevo 2-vverh 3-vpravo 4-vniz
        else:
            turn = 1
        if(check_position(position_x, position_y, array, turn, size) == 0):
            ships_put(array, position_x, position_y, turn, size)
            count += 1
            if count < count_ship:
                return generate_ships(array, count, size, count_ship)

        else:
            return generate_ships(array, count, size, count_ship)


def check_ship(array, x, y):
    if 0 <= x <= 9 and 0 <= y <= 9:
        return array[x][y]
    else:
        return -2


def isDieShips(arr, x, y):
    size_die = 0
    size_live = 0
    size = 0

    res = [[-1 for i in range(2)]for j in range(4)]

    if check_ship(arr, x, y) == 3:
        res[size] = [x, y]
        size_die += 1
        size += 1
#######################
    for i in range(1, 4):
        if(check_ship(arr, x+i, y) == 3):
            res[size] = [x+i, y]
            size_die += 1
            size += 1
        elif(check_ship(arr, x+i, y) == 1):
            size_live += 1
            size += 1
            break
        else:
            break

########################
    for i in range(1, 4):
        if(check_ship(arr, x-i, y) == 3):
            res[size] = [x-i, y]
            size_die += 1
            size += 1
        elif(check_ship(arr, x-i, y) == 1):
            size_live += 1
            size += 1
            break
        else:
            break


########################
    for i in range(1, 4):
        if(check_ship(arr, x, y+i) == 3):
            res[size] = [x, y+i]
            size_die += 1
            size += 1
        elif(check_ship(arr, x, y+i) == 1):
            size_live += 1
            size += 1
            break
        else:
            break

######################
    for i in range(1, 4):
        if(check_ship(arr, x, y-i) == 3):
            res[size] = [x, y-i]
            size_die += 1
            size += 1
        elif(check_ship(arr, x, y-i) == 1):
            size_live += 1
            size += 1
            break
        else:
            break
    if size_live == 0 and size_die == size:
        return res
    else:
        return 0


class ObjWaitPlayer:
    def __init__(self, player):
        self.player = player


class Player:
    def __init__(self, connection, wait):
        self.connection = connection
        self.array = [[0 for i in range(10)] for i in range(10)]
        self.wait = wait
        self.enemy = ''
        self.flag = 0
        self.count_ship = 0

    def generate_pole(self):
        self.count_ship = 0
        for i in range(10):
            for j in range(10):
                self.array[i][j] = 0
        generate_ships(self.array, 0, 4, 1)
        generate_ships(self.array, 0, 3, 2)
        generate_ships(self.array, 0, 2, 3)
        generate_ships(self.array, 0, 1, 4)

    def setEnemy(self, enemy):
        self.enemy = enemy

    def send(self, msg):
        msg += '@'
        self.connection.send(msg.encode('utf-8'))

    def sendShip(self):
        for i in range(10):
            for j in range(10):
                if self.array[i][j] == 1:
                    self.send('ship_add '+str(i) + ' '+str(j))

    def setFlag(self, flag):
        self.flag = flag
        self.send('flag '+str(flag))

    def checkWait(self):
        # add second player ;)
        if len(self.wait) == 0:
            self.wait.append(ObjWaitPlayer(self))
        else:
            self.enemy = self.wait[0].player
            del self.wait[0]
            self.enemy.setEnemy(self)
            self.generate_pole()
            self.enemy.generate_pole()
            self.setFlag(1)
            self.enemy.setFlag(0)
            self.sendShip()
            self.enemy.sendShip()

    def shot(self, x, y):
        if self.array[x][y] == 1:
            self.array[x][y] = 3  # ranen :(
            return 1
        elif self.array[x][y] == 3 or self.array[x][y] == -1:
            return 0
        if self.array[x][y] == 2:
            return 2
        elif self.array[x][y] == 0:
            self.array[x][y] = -1
            return 2

    def check(self, x, y):
        if 0 <= x <= 9 and 0 <= y <= 9:
            return self.array[x][y]

    def isDie(self, x, y):
        res = isDieShips(self.enemy.array, x, y)
        if res != 0:
            for i in range(4):
                if res[i] != [-1, -1]:

                    if self.enemy.check(res[i][0]+1, res[i][1]) == 2:
                        self.enemy.array[res[i][0]+1][res[i][1]] = -1
                        self.send(
                            'bang '+str(res[i][0]+1) + ' '+str(res[i][1]))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]+1) + ' ' + str(res[i][1]))
                    ##########################################
                    if self.enemy.check(res[i][0]-1, res[i][1]) == 2:
                        self.enemy.array[res[i][0]-1][res[i][1]] = -1
                        self.send(
                            'bang '+str(res[i][0]-1) + ' '+str(res[i][1]))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]-1) + ' ' + str(res[i][1]))
                    if self.enemy.check(res[i][0], res[i][1]+1) == 2:
                        self.enemy.array[res[i][0]][res[i][1]+1] = -1
                        self.send(
                            'bang '+str(res[i][0]) + ' ' + str(res[i][1]+1))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]) + ' ' + str(res[i][1]+1))
                    if self.enemy.check(res[i][0], res[i][1]-1) == 2:
                        self.enemy.array[res[i][0]][res[i][1]-1] = -1
                        self.send(
                            'bang '+str(res[i][0]) + ' '+str(res[i][1]-1))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]) + ' ' + str(res[i][1]-1))
                    if self.enemy.check(res[i][0]+1, res[i][1]+1) == 2:
                        self.enemy.array[res[i][0]+1][res[i][1]+1] = -1
                        self.send(
                            'bang '+str(res[i][0]+1) + ' '+str(res[i][1]+1))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]+1) + ' ' + str(res[i][1]+1))
                    if self.enemy.check(res[i][0]+1, res[i][1]-1) == 2:
                        self.enemy.array[res[i][0]+1][res[i][1]-1] = -1
                        self.send(
                            'bang '+str(res[i][0]+1) + ' '+str(res[i][1]-1))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]+1) + ' ' + str(res[i][1]-1))
                    if self.enemy.check(res[i][0]-1, res[i][1]+1) == 2:
                        self.enemy.array[res[i][0]-1][res[i][1]+1] = -1
                        self.send(
                            'bang '+str(res[i][0]-1) + ' '+str(res[i][1]+1))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]-1) + ' ' + str(res[i][1]+1))
                    if self.enemy.check(res[i][0]-1, res[i][1]-1) == 2:
                        self.enemy.array[res[i][0]-1][res[i][1]-1] = -1
                        self.send(
                            'bang '+str(res[i][0]-1) + ' ' + str(res[i][1]-1))
                        self.enemy.send(
                            'enemy_bang '+str(res[i][0]-1) + ' ' + str(res[i][1]-1))

    def isFinish(self):
        count = 0
        for i in range(10):
            for j in range(10):
                if self.array[i][j] == 3:
                    count += 1
        return count == 20

    def process_msg(self):
        receiver = self.connection.recv(256).decode('utf-8')
        if receiver.replace(' ', '') == '':
            raise Exception('Incorect')
        arr_recv = receiver.split(' ')
        if arr_recv[0] == 'click':
            if self.flag != 0:
                return
            if self.enemy == '':
                return

            shot_click = self.enemy.shot(int(arr_recv[1]), int(arr_recv[2]))
            if shot_click == 1:
                # ranen
                res = []
                self.send('ranen '+arr_recv[1] + ' '+arr_recv[2])
                self.enemy.send('enemy_ranen '+arr_recv[1] + ' '+arr_recv[2])
                self.isDie(int(arr_recv[1]), int(arr_recv[2]))
                if self.enemy.isFinish():
                    self.array
                    print('\ENDGAME/')
                    self.send('win')
                    self.enemy.send('lose')

            elif shot_click == 2:
                self.enemy.send('enemy_bang '+arr_recv[1] + ' '+arr_recv[2])
                self.send('bang '+arr_recv[1] + ' '+arr_recv[2])
                self.setFlag(1)
                self.enemy.setFlag(0)
        elif arr_recv[0] == 'ENDGame':
            self.enemy.send('endgame')
            self.connection[0].close()
            self.enemy.connection[0].close()
        elif arr_recv[0] == 'startGame':
            self.checkWait()
