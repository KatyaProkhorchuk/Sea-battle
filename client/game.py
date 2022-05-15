import tkinter as tk
import tkinter.font as tkFont
from base import Base
import time
import socket
from tkinter import messagebox
from threading import Thread
from datetime import datetime
from serverListener import ServerListener




def logger(data):
    try:
        f = open("log.txt","a")
        f.write("["+data+"]\n")
        f.close()
    except:
        pass

def callback_click(i, j, sock):
    def click(event):
        msg = ('click ' + str(i) + ' ' + str(j)).encode('utf-8')
        sock.send(msg)
    return click


def CreateFrame(frame, cell, sock, font, isClick=False):
    for i in range(10):
        arr = []
        for j in range(10):
            button = tk.Button(frame, text='', bg='white',
                               fg='black', height=2, width=2, font=font)
            button.grid(row=i, column=j)
            if isClick:
                button.bind('<Button-1>',callback_click(i,j,sock))
            arr.append(button)#массив кнопок
        cell.append(arr)


class Game(Base):


    def __init__(self, sock, controller):
        Base.__init__(self, sock, controller)
        self.sock = sock
        self.controller = controller
        self.playerShip = []
        self.enemyShip = []
        self.label = tk.Label(text="", font=('Arial', 24), fg='red')
        self.fontStyle = tkFont.Font(size=14)
        self.flag=2
        self.my_flame=tk.Frame()
        self.enemy_frame=tk.Frame()


    def draw(self, window):
        self.my_frame = tk.Frame(window, bg='#2A4480', bd=10,width=2, height=4)
        self.enemy_frame = tk.Frame(window, bg='#2A4480',bd=10, cursor='circle')

        CreateFrame(self.my_frame, self.playerShip,
                    self.sock, self.fontStyle, False)
        CreateFrame(self.enemy_frame, self.enemyShip,
                    self.sock, self.fontStyle, True)

        self.my_frame.grid(row=0, padx=(15,15),column=0, sticky='nsew')
        self.enemy_frame.grid(row=0, padx=(15,15),column=1, sticky='nsew')
        
    def update(self, msg):        
        data = msg.split(' ')
        logger(msg)

        if data[0]=='flag':
            if int(data[1])==0:
                self.enemy_frame.configure(bg='green')
                self.my_frame.configure(bg='#2A4480')
            elif int(data[1])==1:
                self.my_flame.configure(bg='green')
                self.enemy_frame.configure(bg='#2A4480')
        if data[0]=='ship_add':
            i, j = int(data[1]),int(data[2])
            self.playerShip[i][j].configure(bg='#7AA4C2', fg='yellow', text="⚓")
        if data[0]=='ranen':
            i, j = int(data[1]),int(data[2])
            self.enemyShip[i][j].configure(bg='grey', fg='black',text="💣")
        if data[0]=='enemy_ranen':
            i, j = int(data[1]),int(data[2])
            self.playerShip[i][j].configure(bg='grey', fg='black',text="💣")
        if data[0]=='bang':
            i, j = int(data[1]),int(data[2])
            self.enemyShip[i][j].configure(fg='#81CBF5',text="🍩")
        if data[0]=='enemy_bang':
            i, j = int(data[1]),int(data[2])
            self.playerShip[i][j].configure(fg='#81CBF5', text="🍩")
        if data[0]=='win':
            self.controller.changeWindow('Result',msg="You WIN")
        if data[0]=='lose':
            self.controller.changeWindow('Result',msg="You LOSE")
        if data[0] == 'endgame':
            self.controller.changeWindow('Result',msg="Your enemy has left the game⚓")
        

        


        
