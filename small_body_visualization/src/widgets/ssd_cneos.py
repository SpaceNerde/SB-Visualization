import pandas as pd
import tkinter as tk

class SSD_CNEOS:
    def __init__(self, root, data):
        self.root = root
        self.frame = tk.LabelFrame(self.root, labelanchor = tk.N)
        self.df = data
        self.create_table()

    def create_table(self):
        canvas = tk.Canvas(self.root, scrollregion="0 0 2000 1000", width=400, height=400)
        canvas.grid(row=0, column=0, sticky=tk.NSEW)

        scroll = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=canvas.yview)
        scroll.grid(row=0, column=1, sticky=tk.NS)   
        canvas.config(yscrollcommand =scroll.set)
        
        for fila in range(20):
            for col in range(5):
                btn = tk.Button(self.frame, text = f"{fila}-{col}")
                btn.grid(row = fila, column = col, sticky = tk.NSEW)
        '''
        for row in range(len(self.df)):
            for column in range(len(self.df.columns)):
                e = tk.Entry(self.frame, fg='blue', font=('Arial', 16, 'bold'))
                e.grid(row=row, column=column, sticky=tk.NSEW)
        '''
        item = canvas.create_window(( 2, 2 ), anchor = tk.NW,  window = self.frame )
      
        
        
        

        