import tkinter as tk
from PIL import Image, ImageTk

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size= 32, color1="white", color2= "blue"):
        '''size is the size of the board, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size