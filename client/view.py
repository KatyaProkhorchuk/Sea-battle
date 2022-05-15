import tkinter as tk
from game import Game
from start import Start
from result import Result


class View:
    def __init__(self, window, sock):
        self.window = window
        self.sock = sock
        self.view = self.createWindow('Conn')


    def createWindow(self,name, msg=''):
        if name == 'Conn':
            return Start(self.sock, self)
        if name == 'Game':
            return Game(self.sock, self)
        if name == 'Result':
            return Result(self.sock, self,msg)


    def clear(self):
        root=self.window.grid_slaves()
        for obj in root:
            obj.destroy()


    def changeWindow(self, name, msg=''):
        self.clear()
        self.view = self.createWindow(name,msg)
        self.view.draw(self.window)
        

    def update(self,name):
        self.view.update(name)
