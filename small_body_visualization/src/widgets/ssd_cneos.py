import pandas as pd
import tkinter as tk

class SSD_CNEOS:
    def __init__(self, root, data):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.df = data
        self.create_table()

    def create_table(self):
        print(self.df.shape)
        for row in range(len(self.df)):
            for column in range(len(self.df.columns)):
                e = tk.Entry(self.root, width=10, fg='blue', font=('Arial', 16, 'bold'))
                e.grid(row=row, column=column)
    
        