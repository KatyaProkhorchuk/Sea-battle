import tkinter as tk
from tkinter import messagebox
import socket
from view import View
from serverListener import ServerListener
from PIL import Image, ImageTk
import sys
import time
import os


window = tk.Tk()
window.title("Морской бой")
window.resizable(width=False, height=False)
window.geometry('1200x680')
img = ImageTk.PhotoImage(Image.open(os.path.dirname(__file__)+"/resource/background.png"))
background_label = tk.Label(window, image=img)
background_label.place(x=0, y=0)


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 12335))
    view = View(window, sock)
    view.changeWindow('Conn')
    ServerListener(view, sock).start()
except:
    view = View(window, '')
    view.changeWindow('Err')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        try:
            sock.send('ENDGame'.encode('utf-8'))
            time.sleep(0.5)
            sock.close()
            window.destroy()
            sys.exit()
        except Exception:
            sys.exit()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
