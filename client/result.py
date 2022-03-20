import tkinter as tk
from base import Base



def callback_click(sock, controller):
    def click(event):    
        controller.changeWindow('Game')
        sock.send('startGame'.encode('utf-8'))

    return click


class Result(Base):

    def __init__(self, userSocket, controller, msg=''):
        Base.__init__(self, userSocket, controller, msg)
        self.res = ''

    def draw(self, window):
        print ('res')
        frame = tk.Frame(window, bg='#42e3f5',width=2,height=4)
        frame.place(anchor="c",relx=.5, rely=.5)
        name = tk.Label(frame, text=self.msg,bg='#42e3f5', font=("Arial",25),
                        height=2, width=20)
        # start_game_button = tk.Button(
            # frame, text='New game', bg='#42b6f5', fg='black', height=2, width=20, cursor='circle')
        # start_game_button.bind(
        #     '<Button-1>', callback_click(self.sock, self.controller))
        name.pack(pady=(50, 50),padx=(50,50), fill=tk.X,)
        # start_game_button.pack(fill=tk.BOTH)
        frame.grid(row=0,column=0,padx=(400,400),pady=(250,250))
        

