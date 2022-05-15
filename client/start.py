import tkinter as tk
from PIL import Image, ImageTk
from base import Base


def callback_click(sock, controller):
    def click(event):    
        controller.changeWindow('Game')
        sock.send('startGame'.encode('utf-8'))
    return click

class Start(Base):
    def __init__(self, sock, controller):
        Base.__init__(self, sock, controller)

    def draw(self, window):
        frame = tk.Frame(window, bg='#2A4480',width=1,height=1)
        frame.place(anchor="c",relx=.5, rely=.5)
        name = tk.Label(frame, text='Морской Бой',bg='#2A4480',fg ='white', font=("Arial",25),
                        height=2, width=20)
        start_game_button = tk.Button(
            frame, text='START', bg='#2A4480', fg='white', height=2, width=20, cursor='circle')
        start_game_button.bind(
            '<Button-1>', callback_click(self.sock, self.controller))
       
        name.pack(pady=(50, 50),padx=(50,50), fill=tk.X,)
        start_game_button.pack(fill=tk.BOTH)
        frame.grid(row=0,column=0,padx=(400,400),pady=(250,250)) 
