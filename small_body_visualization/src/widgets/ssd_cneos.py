import pandas as pd
import tkinter as tk

class SSD_CNEOS(tk.Frame):
    def __init__(self, root, data, *args):
        super().__init__(root, *args)

        self.entries = []
        self.df = data
        self.root = root

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        
        self.create_table()  

        for entry in self.entries:
            entry.bind("<Configure>", self.update_canvas_width())
        
    def data_processing(self, e, r, c):
        value = e.widget.get()
        self.df.iloc[r,c] = value

    def create_table(self):
        rows, cols = self.df.shape
        i = 0

        for col in self.df.columns:
            e = tk.Entry(self.frame)
            e.insert(0, col)
            e.grid(row=0, column=i)
            i += 1
            self.entries.append(e)

        for r in range(rows):
            for c in range(cols):
                e = tk.Entry(self.frame)
                e.insert(0, self.df.iloc[r, c])
                e.grid(row=r+1, column=c)
                e.bind('<KeyRelease>', lambda event, y=r, x=c: self.data_processing(event, y,x))
                
                
    def update_canvas_width(self):
        total_width = sum(entry.winfo_width()*124 for entry in self.entries)
        self.canvas.config(scrollregion=(0, 0, total_width, self.canvas.winfo_height()))
        self.canvas.config(width=total_width)