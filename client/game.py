import tkinter as tk
import tkinter.font as tkFont
from base import Base
import time
import socket
from tkinter import messagebox
from threading import Thread
from datetime import datetime
from serverListener import ServerListener

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

temp = 0
h,m,s = 0, 0, 0
after_id = ''
def coord(data):
    result = data.split(' ')
    return int(result[0]), int(result[1])
def timer(game):
        global temp, after_id
        t_temp=datetime.fromtimestamp(temp).strftime("%H:%M:%S")
        game.configure(text=str(t_temp))
        temp+=1
class Game(Base):
    def __init__(self, sock, controller):
        Base.__init__(self, sock, controller)
        self.sock = sock
        self.controller = controller
        self.playerShip = []
        self.enemyShip = []
        self.label = tk.Label(text="", font=('Arial', 24), fg='red')
        self.informationLabel = tk.Label()
        self.fontStyle = tkFont.Font(size=14)
        self.flag=2
        self.my_flame=tk.Frame()
        self.enemy_frame=tk.Frame()
        self.time_and_info=tk.Frame()
        self.time=tk.Label()
    def draw(self, window):
        
        self.my_frame = tk.Frame(window, bg='#0d00ff', bd=10,width=2, height=4)
        self.enemy_frame = tk.Frame(window, bg='#0d00ff',bd=10, cursor='circle')
        self.time_and_info=tk.Frame(window, bg='red', bd=10,width=300, height=50)
        CreateFrame(self.my_frame, self.playerShip,
                    self.sock, self.fontStyle, False)
        CreateFrame(self.enemy_frame, self.enemyShip,
                    self.sock, self.fontStyle, True)
        self.time = tk.Label(self.time_and_info, text='', bg='white',
                               fg='black', height=1, width=1, font=self.fontStyle)
        self.time.grid(sticky='nsew')
        
        self.my_frame.grid(row=0, padx=(15,15),column=0, sticky='nsew')
        self.enemy_frame.grid(row=0, padx=(15,15),column=1, sticky='nsew')
        self.time_and_info.grid(row=0,padx=(1,1),column=2,sticky=tk.NE)
        
    def update(self, msg):        
        data = msg.split(' ')
        print(data)
        if data[0]=='flag':
            if int(data[1])==0:
                self.time.configure(bg='green')
           
            elif int(data[1])==1:
                self.time.configure(bg='red')
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
            # messagebox.showinfo("EndGame","You WIN")
            # if messagebox.askokcancel("ok", "You WIN"):
            #     self.window.close()
            print('win')
            self.controller.changeWindow('Result',msg="You WIN")
            # self.controller.changeWindow('Result',text='You WIN')
        if data[0]=='lose':
            print('lose')
            self.controller.changeWindow('Result',msg="You LOSE")

            # messagebox.showinfo("EndGame","You LOSE")
            # self.controller.changeWindow('Conn')
        

        


        
