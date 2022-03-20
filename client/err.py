import tkinter as tk
from base import Base

class Err(Base):
    def __init__(self,window,sock):
        super().__init__(window,sock)
        self.window = window
        self.draw()
    def draw(self):
        pass
        
    def render(self):
        pass