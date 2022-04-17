import tkinter as tk
from PIL import Image, ImageTk
from base import Base


def callback_click(sock, controller):
    def click(event):    
        controller.changeWindow('Game')
        sock.send('startGame'.encode('utf-8'))

    return click


def show_image(path, root):
    # pass
    img = Image.open(path)
    width = 500
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    imag = img.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(imag)
    panel = tk.Label(root, image=image)
    panel.pack(side="top", fill="both", expand="no")

    # tk.Button(root, text='Quit', command=root.quit).place(x=250, y=250)


class Start(Base):
    def __init__(self, sock, controller):
        Base.__init__(self, sock, controller)

    def draw(self, window):
        frame = tk.Frame(window, bg='#42e3f5',width=2,height=4)
        frame.place(anchor="c",relx=.5, rely=.5)
        name = tk.Label(frame, text='Морской Бой',bg='#42e3f5', font=("Arial",25),
                        height=2, width=20)
        start_game_button = tk.Button(
            frame, text='Start', bg='#42b6f5', fg='black', height=2, width=20, cursor='circle')
        start_game_button.bind(
            '<Button-1>', callback_click(self.sock, self.controller))
        name.pack(pady=(50, 50),padx=(50,50), fill=tk.X,)
        start_game_button.pack(fill=tk.BOTH)
        frame.grid(row=0,column=0,padx=(400,400),pady=(250,250))
