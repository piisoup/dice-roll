from tkinter import *
import random

class diceroll:

    def __init__(self, root):
        self.root = root
        root.title("Dice roll")
        root.geometry("600x200")
        root.resizable("0,0")

        self.count = 0
        self.num1 = 0
        self.num1 = 0

        bg_color = " #f77f77"
        style = "Arial 20"

        Button(root, text = "quit", font = style, command = self.generate_random, width=17).grid(row=0, columns=1, padx=0, pady=0)

        self.box1 = Label(self.root )